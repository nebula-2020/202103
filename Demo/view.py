# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Demo.util.web import response_json
from Demo.service.userService import add_user
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


def sign_in(request):
    req_id = request.GET.get('id')
    req_password = request.GET.get('password')
    conn = get_redis_connection('default')
    return HttpResponse('hello_ world')


def sign_up(request):
    ret = None
    if(request.method == 'POST'):
        req = json.loads(request.body)
        req_pwd = req['password']
        req_ph = req['phone']
        req_n = req['name']
        ret = add_user(phone=req_ph, password=req_pwd, name=req_n)
    su = ret is not None
    if su:
        ret = {'id': ret.id}
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
