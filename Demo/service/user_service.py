# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Demo.util.common import *
from Demo.util.const import *
from Demo.entity import *
import Demo.util.repository as repo
import re
import traceback


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
    if not all_not_None(password, id):
        return 0
    if not re.match(RE_PASSWORD, password):
        return 0
    if id == '':
        return 0
    res = repo.get(User, id=id)
    if res is not None:
        ret = res.id
    else:
        ret = 0
    return ret  # 返回id
