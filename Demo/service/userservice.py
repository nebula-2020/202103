# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
用户服务。
'''
# from django.http.request import HttpRequest
# from django.http.response import HttpResponseRedirect
# from Demo.util.session import get_session, set_session
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
    if not all_not_None(password, phone, name):
        return None
    if exist((password, phone, name), ('')):
        return None
    if not re.match(RE_MOBILE, phone):
        return None
    if not re.match(RE_PASSWORD, password):
        return None
    ret = None
    try:
        found = repo.get(User, phone=phone)
        if found == None:
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
    if not all_not_None(password, id):  # 传入空值
        return 0
    if not re.match(RE_PASSWORD, password):  # 密码格式错误
        return 0
    if id <= 0:  # ID错误
        return 0
    res = repo.get(User, id=id)
    if res is not None and type(res.id) == int and res.id > 0:
        ret = res.id
    else:  # 用户不存在
        ret = 0
    return ret  # 返回id


# def login_verify(login_url: str = '/signIn', tag: str = 'id'):
#     """装饰器，用户登陆Session验证。

#     Parameters
#     ----------
#     login_url : str, optional
#         若用户未登录则跳转至此, by default '/signIn'
#     tag : str, optional
#         Cookies中用户ID所在的键值对的键名，如果缓存中也有这个键对应的值则认为已经登录, by default 'id'
#     """
#     def decorator(func):
#         @wraps(func)
#         def wrap(request: HttpRequest, *args, **kwargs):
#             sign = True
#             if tag in request.COOKIES:
#                 id_str = base62(request.COOKIES[tag])
#                 val = get_session(id_str)  # 获取session中的用户ID为键的值
#                 print(val)
#                 if bool(id_str) == True:
#                     set_session(id_str, True)  # 时间调最大
#                     sign = False
#                     return func(request, *args, **kwargs)
#             if sign:  # 登录过期请重新登陆
#                 # 获取用户当前访问的url，并传递给/user/login/
#                 next = request.get_full_path()
#                 res = ''.join([login_url, '?next=', next])
#                 ret = HttpResponseRedirect(res)
#                 return ret
#         return wrap
#     return decorator


@type_checking
def about_me(id: int) -> dict:
    """获取用户详情，查两个表。

    Parameters
    ----------
    id : int
        ID

    Returns
    -------
    dict
        指定ID用户详情。

        字段：
        * id：ID
        * phone：手机号
        * create_time：创建时间
        * name：昵称
        * ps：个性签名
        * icon：头像路径
    """
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


@type_checking
def get_detials(id: int) -> dict:
    """获取用户介绍，查一个表。

    Parameters
    ----------
    id : int
        ID

    Returns
    -------
    dict
        指定ID用户详情。

        字段：
        * id：ID
        * create_time：创建时间
        * name：昵称
        * ps：个性签名
        * icon：头像路径
    """
    if id > 0:
        detials = repo.get(UserDetials, id=id)
        if detials is not None:
            t = detials.create_time.timetuple()
            return {
                'id': id,
                'create_time': int(time.mktime(t)*1000),
                'name': detials.name,
                'ps': detials.ps,
                'icon': detials.icon,
            }
    return {'id': 0}
