from Demo.entity import User
import Demo.repository.util
from django.http import HttpResponse
from Demo.repository.util import *
from django.shortcuts import *
import json


def index(request):
    return render(request, "index.html")


def test(request):
    print('REQ')
    return render(request, "index.html")


def sign_in(request):
    req_id = request.GET.get('id')
    req_password = request.GET.get('password')
    return HttpResponse('hello_ world')


def get_users(request):
    users = exec(User, 'select * from user')
    res = []
    for ele in users:
        res.append({'id': ele.id, 'name': ele.name, 'phone': ele.phone,
                    'password': ele.password})
    res = json.dumps(res)
    return HttpResponse(res)


def delete_user(request):
    req_id = request.GET.get('id')
    delete(User, id=req_id)
    return HttpResponse()


def update_user(request):
    req_pwd = request.GET.get('password')
    req_ph = request.GET.get('phone')
    req_n = request.GET.get('name')
    req_id = request.GET.get('id')
    print(req_id)
    if req_pwd != '' and req_ph != '' and req_n != '':
        if req_id == '' or req_id is None:
            User.objects.create(password=req_pwd, phone=req_ph, name=req_n)
        else:
            update(User, {'id': req_id}, {
                   'password': req_pwd, 'phone': req_ph, 'name': req_n})
    new = Demo.repository.util.find(User, phone=req_ph)
    return HttpResponse(new)
