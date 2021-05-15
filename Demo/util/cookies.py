# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Cookie常见操作。
'''
from django.http import *


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
    str, HttpResponse
        加密盐，已经设置过cookie的参数
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


def get_cookie(req: HttpRequest, key: str):
    """获取一条cookie。

    Parameters
    ----------
    resp : HttpRequest
        一个基本的HTTP请求
    key : str
        键

    Returns
    -------
    str
        如果获取失败则返回空字符串
    """
    if key in req.COOKIES:
        return request.COOKIES[key]
    return ''


def set_cookie(resp: HttpResponse, key: str, value: str) -> HttpResponse:
    """设置cookie。

    Parameters
    ----------
    resp : HttpResponse
        以字符串作为内容的HTTP响应类
    key : str
        键
    value : str
        cookie值

    Returns
    -------
    HttpResponse
        已经设置过cookie的参数
    """
    resp.set_cookie(key=key, value=value)
    return resp
