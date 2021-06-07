# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Session常见操作。
'''
from django.core.cache import cache  # 已经配置redis


def set_cache(key: str, value, time: int = 1800):
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


def get_cache(key: str) -> str:
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


def delete_cache(key: str):
    """删除一条缓存。

    Parameters
    ----------
    key : str
        键
    """
    set_cache(key, '', 1)


def verify(data: dict) -> bool:
    """判断字典中的值是否与缓存中的匹配。

    Parameters
    ----------
    data : dict
        字典，将检查其中所有键，这些键必须全部在缓存中并且每一个键对应的值与缓存中存储的数据完全一致

    Returns
    -------
    bool
        描述验证成功与否。
    """
    for key in data.keys():
        c = get_cache(key)
        if c != data[key]:
            return False
    return True
