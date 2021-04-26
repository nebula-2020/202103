# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
视图。
'''
from Demo.util.common import *
from Demo.util.web import *
import Demo.service.user_service as us
from Demo.entity import User
import Demo.util.repository as repo
from django.http import HttpResponse
from django.shortcuts import *
import json

from django_redis import get_redis_connection


def index(request):
    return render(request, "index.html")


def test(request):
    print('test')
    return HttpResponse('data')


@req_type('POST')
def sign_in(request):
    req = get_postbody(request)
    id = int(req['id'])
    phone = req['phone']
    pwd = req['password']
    if phone is not None and phone != '':
        res = us.login(phone=phone, password=pwd)
    elif id is not None and id > 0:
        res = us.login(id=id, password=pwd)
    else:
        res = None
    # conn = get_redis_connection('default')
    su = res > 0
    ret = HttpResponse(response_json(succeed=su, values=res if su else 0))
    return ret


@req_type('POST')
def sign_up(request):
    req = get_postbody(request)
    req_pwd = req['password']
    req_ph = req['phone']
    req_n = req['name']
    ret = us.add_user(phone=req_ph, password=req_pwd, name=req_n)
    su = ret is not None
    if su:
        ret = {'id': ret.id}
        us.login(id=ret, password=req_pwd)
    ret = HttpResponse(response_json(succeed=su, values=ret))
    print(ret)
    return ret


def get_users(request):
    users = exec(User, 'select * from user')
    res = []
    for ele in users:
        res.append({'id': ele.id, 'name': ele.name, 'phone': ele.phone,
                    'password': ele.password})
    res = json.dumps(res)
    ret = HttpResponse(res)
    return ret


def delete_user(request):
    req_id = request.GET.get('id')
    repo.delete(User, id=req_id)
    return HttpResponse()
