# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
视图。
'''
from Demo.util.common import *
from Demo.util.web import *
import Demo.service.user_service as us
from Demo.entity import *
import Demo.util.repository as repo
from django.http import HttpResponse
from django.shortcuts import *
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, "index.html")


@require_http_methods(["POST"])
def sign_in(request):
    req = get_postbody(request)
    id = int(req['id'])
    phone = req['phone']
    pwd = req['password']
    if id is not None and id > 0:
        res_id = us.login(id=id, password=pwd)
    elif phone is not None and phone != '':
        res_id = us.login(phone=phone, password=pwd)
    else:
        res_id = 0
    su = res_id > 0
    json_str = str(res_id if su else 0)
    ret = HttpResponse(json_str, status=200 if su else 403)
    # cookie_str = json.dumps({})
    if res_id > 0:
        ret.set_cookie(key=COOKEY, value=res_id)
        # ret.set_cookie(key=COOKIE_ICON, value=us.)  # 获取头像
    set_session(base62(res_id), True)
    return ret


@require_http_methods(["POST"])
def sign_up(request):
    req = get_postbody(request)
    req_pwd = req['password']
    req_ph = req['phone']
    req_n = req['name']
    ret = us.add_user(phone=req_ph, password=req_pwd, name=req_n)
    su = ret is not None
    if su:
        us.login(id=ret.id, password=req_pwd)
        ret = {'id': ret.id}
        ret = json.dumps(ret, default=None, sort_keys=False)
        ret = HttpResponse(ret, status=200)
    else:
        ret = HttpResponse(status=403)
    return ret


@us.login_verify(tag=COOKEY)
@require_http_methods(["POST"])
def user_center(request: HttpRequest):
    req = get_postbody(request)
    id = 1  # int(req['id'])
    res = us.about_me(id)
    if res['id'] == id:
        res = json.dumps(res, default=None, sort_keys=False)
        ret = HttpResponse(res, status=200)
    else:
        ret = HttpResponse(status=403)
    return ret


@us.login_verify(tag=COOKEY)
@require_http_methods(["POST"])
def get_users(request: HttpRequest):
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
