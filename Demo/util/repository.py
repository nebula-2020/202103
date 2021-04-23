# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import *


def exec(clazz: Model, sql: str):
    res = clazz.objects.raw(sql)
    ret = []
    for ele in res:
        ret.append(ele)
    return ret

def get(clazz: Model, **kwargs):
    try:
        ret = clazz.objects.get(**kwargs)
    except:
        ret=None
    return ret

def find(clazz: Model, **kwargs):
    res = clazz.objects.filter(**kwargs)
    ret = []
    print(type(res))
    for ele in res:
        ret.append(ele)
    return ret


def delete(clazz: Model, **kwargs):
    obj = clazz.objects.get(**kwargs)
    obj.delete()


def update(clazz: Model, find: dict, update: dict):
    clazz.objects.filter(**find).update(**update)
    # for ele in res:
    #     for k, v in update.items():
    #         setattr(ele, k, v)
    #         pass
    #     for k, v in update.items():
    #         print(getattr(ele, k))
    #         pass
    #     ele.save()
    #     pass
    # res.update()
    pass
