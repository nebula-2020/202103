# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from Demo.util.const import *
import json


def response_json(succeed: bool, values):
    res = {}
    res[RESPONSE_STATUS] = succeed
    res[RESPONSE_DATA] = values
    return json.dumps(res, default=None, sort_keys=False)


def set_cookie(resp: HttpResponse, key, value):
    salt = str(key)+''
    resp.set_signed_cookie(key, value, salt=salt)
    return salt, resp
