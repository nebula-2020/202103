#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
用户数据表。
'''
from django.db.models import *


class User(Model):
    id = BigIntegerField(verbose_name='账号', primary_key=True)
    name = CharField(verbose_name='昵称', max_length=20, null=False)
    password = CharField(verbose_name='密码', max_length=30, null=False)
    phone = CharField(verbose_name='手机号', null=False,
                      unique=True, max_length=15)
    create_time = DateTimeField(auto_now_add=True, null=False)

    # 指定表名
    class Meta:
        db_table = 'user'
