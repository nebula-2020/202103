# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
RE_MOBILE = r"^\d{4,15}$"
RE_PASSWORD = r"^(?=.*\d)(?=.*[a-zA-Z])(?=.*[\`~!@#$%^&*\-=_\+\[\]\\\|\{\}:;\"\'<>,\56?/])[\da-zA-Z\`~!@#$%^&*\-=_\+\[\]\\\|\{\}:;\"\'<>,\56?/]{8,20}$"
RESPONSE_STATUS = 'succeed'
RESPONSE_DATA = 'data'
COOKEY = 'index'
COOKIE_ICON = 'icon'
print(re.match(RE_PASSWORD, '11q11111'))
print(re.match(RE_PASSWORD, '11q1111/'))
