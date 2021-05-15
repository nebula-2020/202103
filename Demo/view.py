# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
视图。
'''
from Demo.util import const
import Demo.util.cookies as cs
import Demo.util.token as tk
import json

from django.http import *
from django.shortcuts import *
from django.views.decorators.http import require_http_methods

import Demo.service.userservice as us
import Demo.util.repository as repo
from Demo.entity import *
from Demo.util.common import *


def index(request):
    return render(request, "index.html")


@require_http_methods(["POST"])
def sign_up(request):
    """新用户注册视图。

        Parameters
        ----------
        request : HttpRequest
            一个基本的HTTP请求

        Returns
        -------
        HttpResponse
            以字符串作为内容的HTTP响应类。
    """
    req = json.loads(request.body)
    req_pwd = req['password']
    req_ph = req['phone']
    req_n = req['name']
    ret = us.add_user(phone=req_ph, password=req_pwd, name=req_n)
    if ret is not None:  # 注册成功
        us.login(id=ret.id, password=req_pwd)
        ret = JsonResponse({'id': ret.id}, status=200)
    else:
        ret = HttpResponse(status=403)
    return ret


@require_http_methods(["POST"])
def sign_in(request):
    req = json.loads(request.body)
    id = int(req['id'])
    phone = req['phone']
    pwd = req['password']
    if id is not None and id > 0:
        res_id = us.login(id=id, password=pwd)
    elif phone is not None and phone != '':
        res_id = us.login(phone=phone, password=pwd)
    else:
        res_id = 0
    if res_id > 0:
        request.session[const.SESSION_UID] = res_id
        ret = HttpResponse(str(res_id), status=200)  # 只传一个数字，不是json
        ret = cs.set_cookie(ret, key=const.COOKEY_UID, value=str(res_id))
        #  cookie存储10进制账号，session中存储62进制账号
    else:
        ret = HttpResponse(str(0), status=403)
    return ret


@require_http_methods(["GET", "POST"])
def get_icon(request):
    id = request.session[const.SESSION_UID]
    if id is not None and id > 0:
        d = us.get_detials(id)
        if d['id'] == id:
            ret = HttpResponse(status=200)
            ret = cs.set_cookie(ret, key=const.COOKIE_ICON, value=d['icon'])
        else:
            ret = HttpResponse(status=403)
    else:
        ret = HttpResponse(status=403)
    return ret


@require_http_methods(["POST", "GET"])
def user_center(request: HttpRequest):
    id = request.session[const.SESSION_UID]  # int(req['id'])
    res = us.about_me(id)
    if res['id'] == id:
        ret = JsonResponse(res, status=200)
    else:
        ret = HttpResponse(status=403)
    return ret


# @us.login_verify(tag=const.COOKEY)
@require_http_methods(["POST", "GET"])
def get_users(request):
    users = exec(User, 'select * from user')
    res = []
    for ele in users:
        res.append({'id': ele.id, 'name': ele.name, 'phone': ele.phone,
                    'password': ele.password})
    ret = JsonResponse(res, safe=False)
    return ret


def delete_user(request):
    req_id = request.GET.get('id')
    repo.delete(User, id=req_id)
    return HttpResponse()
