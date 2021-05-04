# !/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import inspect
from functools import wraps
import traceback


def all_not_None(*args) -> bool:
    for ele in args:
        if ele is None:
            return False
    return True


def type_checking(func):
    signature = inspect.signature(func)
    params = signature.parameters  # 参数有序字典
    keys = tuple(params.keys())

    @wraps(func)
    def wrap(*args, **kwargs):
        CheckItem = collections.namedtuple('CheckItem', ('a', 'k', 'v'))
        check_list = []
        for i, v in enumerate(args):
            k = keys[i]
            anno = params[k].annotation
            if anno is not inspect._empty:
                check_list.append(CheckItem(a=anno, k=k, v=v))
        for i, v in kwargs.items():
            if i in params:
                anno = params[i].annotation
                if anno is not inspect._empty:
                    check_list.append(CheckItem(a=anno, k=i, v=v))
        for e in check_list:
            if not isinstance(e.v, e.a):
                msg = 'The type of argument {arg} expected {exp!r}, got {got!r}'
                err = msg.format(exp=e.a.__name__, arg=e.k,
                                 got=type(e.v).__name__)
                raise TypeError(err)
        return func(*args, **kwargs)
    return wrap

def base62(val:int)->str:
    try:
        if type(val )is not int:
            v=int(val)
        else:
            v=val
        num_str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if val == 0:
            return '0'
        base36 = []
        n=val
        while n != 0:
            n, r = divmod(n, 62) 
            base36.append(num_str[r])

        return ''.join(reversed(base36))
    except:
        traceback.print_exc()
