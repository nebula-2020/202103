# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from Demo.util.const import *
import json
from functools import wraps
import inspect
import collections
from django.core.cache import cache  # 已经配置redis


def get_postbody(request):
    req = None
    if(request.method == 'POST'):
        req = json.loads(request.body)
    return req


# def response_json(succeed: bool, values):
#     res = {}
#     res[RESPONSE_STATUS] = succeed
#     res[RESPONSE_DATA] = values
#     return json.dumps(res, default=None, sort_keys=False)


def set_signed_cookie(resp: HttpResponse, key: str, value: str, time: int = 86400):
    """设置cookie。

    Parameters
    ----------
    resp : HttpResponse
        以字符串作为内容的HTTP响应类
    key : str
        键
    value : str
        cookie值
    time : int, optional
        以秒为单位的cookie生存时间, by default 86400

    Returns
    -------
    str
        加密盐
    HttpResponse
        已经设置过cookie的参数
    """
    if resp is not None and key is not None and key != '':
        salt = str(key)+''
        resp.set_signed_cookie(key, value, salt=salt, max_age=time)
        return salt, resp
    else:
        raise ValueError('Arguments contains None.')


def get_signed_cookie(req: HttpRequest, key: str, salt: str) -> str:
    """获取一条cookie。

    Parameters
    ----------
    resp : HttpRequest
        一个基本的HTTP请求
    key : str
        键
    salt : str
        加密盐

    Returns
    -------
    str
        如果获取失败则返回空字符串
    """
    return req.get_signed_cookie(key=key, default='', salt=salt)


def set_session(key: str, value, time: int = 1800):
    """设置一条缓存。

    Parameters
    ----------
    key : str
        键
    value : Any
        缓存值
    time : int, optional
        缓存保持时间，单位为秒, by default 1800
    """
    cache.set(key.encode('utf-8'), value, time)
    pass


def get_session(key: str) -> str:
    """获得缓存指定值。

    Parameters
    ----------
    key : str
        键

    Returns
    -------
    str
        缓存值，若不存在则返回```None```
    """
    ret = None
    if cache.has_key(key):
        ret = cache.get(key)
    return ret


def delete_session(key: str):
    """删除一条缓存。

    Parameters
    ----------
    key : str
        键
    """
    set_session(key, '', 10)
