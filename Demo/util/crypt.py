# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
加密与解密。
'''
from django.core import signing


def encrypt(obj, key: str, salt: str) -> str:
    """加密。

    Parameters
    ----------
    obj : 
        明文
    key : str
        密钥
    salt : str
        加密盐

    Returns
    -------
    str
        密文。
    """
    value = signing.dumps(obj, key=key, salt=salt)
    value = signing.b64_encode(value.encode()).decode()
    return value


def decrypt(src: str, key: str, salt: str) -> tuple:
    """解密。

    Parameters
    ----------
    src : str
        密文
    key : str
        密钥
    salt : str
        加密盐

    Returns
    -------
    tuple
        (明文,明文的类型)。
    """
    src = signing.b64_decode(src.encode()).decode()
    raw = signing.loads(src, key=key, salt=salt)
    return raw, type(raw)
