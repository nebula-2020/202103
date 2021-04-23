# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Demo.util.const import *
from Demo.entity import *
import Demo.util.repository as repo
import re
import traceback


def add_user(phone: str, password: str, name: str) -> User:
    ret = None
    if password != None and phone != None and name != None:
        if password != '' and phone != '' and name != '':
            if re.match(RE_MOBILE, phone) and re.match(RE_PASSWORD, password):
                try:
                    found = repo.get(User, phone=phone)
                    if(found is None):
                        User.objects.create(password=password, phone=phone)
                        ret = repo.get(User, phone=phone)
                except:
                    traceback.print_exc()
                    pass
    return ret
