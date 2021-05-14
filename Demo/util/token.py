# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Token常见操作。
'''
import Demo.util.crypt as crypt
import hashlib

'''
sub	用户名
crt	生成时间
role	角色
auth	权限
'''


def create(header, string: str, key: str, salt: str) -> str:
    """创建Token。

    Parameters
    ----------
    header : 
        请求头
    string : str
        用于Token的信息
    key : str
        密钥
    salt : str
        加密盐

    Returns
    -------
    str
        Token。
    """
    payload = crypt. encrypt(string, key, salt)
    md5 = hashlib.md5()
    encrypted_header = crypt. encrypt(header)
    md5.update(string.encode())
    signature = md5.hexdigest()
    ret = "%s.%s.%s" % (encrypted_header, payload, signature)
    return ret


def verify(token: str, key: str, salt: str) -> tuple:
    """创建Token。

    Parameters
    ----------
    token : str
        Token
    key : str
        密钥
    salt : str
        加密盐

    Returns
    -------
    list
        (请求头,Token信息,签名)
    """
    ret = str(token).split('.')
    for i in range(len(ret)):
        ret[i] = crypt. decrypt(ret[i], key, salt)
    return tuple(ret)
