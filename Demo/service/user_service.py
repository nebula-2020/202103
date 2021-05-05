# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from Demo.util.web import get_session, set_session
from Demo.util.common import *
from Demo.util.const import *
from Demo.entity import *
import Demo.util.repository as repo
import re
import traceback
import time


@type_checking
def add_user(phone: str, password: str, name: str) -> User:
    """添加用户。

    Parameters
    ----------
    phone : str
        手机号
    password : str
        密码
    name : str
        昵称

    Returns
    -------
    User
        插入后会从数据库读取这个用户。
    """
    if password == None or phone == None or name == None:
        return None
    if password == '' or phone == '' or name == '':
        return None
    if not re.match(RE_MOBILE, phone):
        return None
    if not re.match(RE_PASSWORD, password):
        return None
    ret = None
    try:
        found = repo.get(User, phone=phone)
        if(found is None):
            User.objects.create(password=password, phone=phone)
            ret = repo.get(User, phone=phone)
            UserDetials.objects.create(id=ret.id, name=name)
    except:
        traceback.print_exc()
        pass
    return ret


@type_checking
def login(password: str,  id: int = 0) -> int:
    """账号(ID)密码登录服务。

    Parameters
    ----------
    password : str
        密码
    id : int, optional
        用户ID, by default 0

    Returns
    -------
    int
        用户ID
    """
    if not all_not_None(password, id):
        return 0
    if not re.match(RE_PASSWORD, password):
        return 0
    if id <= 0:
        return 0
    res = repo.get(User, id=id)
    if res is not None and type(res.id) is int and res.id > 0:
        ret = res.id
    else:
        ret = 0
    return ret  # 返回id


@type_checking
def verify(id: int) -> bool:
    """用户登录验证，缓存中有无用户记录。

    Parameters
    ----------
    id : int
        用户ID

    Returns
    -------
    bool
        描述验证成功与否
    """
    id_str = base62(id)
    val = get_session(id_str)
    print(val)
    if bool(id_str) == True:
        set_session(id_str, True)
        return True
    else:
        return False  # 登录过期请重新登陆


def login_verify(login_url: str = '/signIn', tag: str = 'id'):
    """用户登陆验证。

    Parameters
    ----------
    login_url : str, optional
        若用户未登录则跳转至此, by default '/signIn'
    tag : str, optional
        Cookies中用户ID所在的键值对的键名, by default 'id'
    """
    def decorator(func):
        @wraps(func)
        def wrap(request: HttpRequest, *args, **kwargs):
            if tag in request.COOKIES and verify(int(request.COOKIES[tag])):
                return func(request, *args, **kwargs)
            else:
                # 获取用户当前访问的url，并传递给/user/login/
                next = request.get_full_path()
                res = ''.join([login_url, '?next=', next])
                ret = HttpResponseRedirect(res)
                return ret
        return wrap
    return decorator


@type_checking
def about_me(id: int) -> dict:
    if id > 0:
        user = repo.get(User, id=id)
        if user is not None:
            detials = repo.get(UserDetials, id=id)
            if detials is not None:
                t = detials.create_time.timetuple()
                return {
                    'id': user.id,
                    'phone': user.phone,
                    'create_time': int(time.mktime(t)*1000),
                    'name': detials.name,
                    'ps': detials.ps,
                    'icon': detials.icon,
                }
    return {'id': 0}
