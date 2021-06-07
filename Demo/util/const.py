# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 服务

RE_MOBILE = r"^\d{4,15}$"
RE_PASSWORD = r"^(?=.*\d)(?=.*[a-zA-Z])(?=.*[\`~!@#$%^&*\-=_\+\[\]\\\|\{\}:;\"\'<>,\56?/])[\da-zA-Z\`~!@#$%^&*\-=_\+\[\]\\\|\{\}:;\"\'<>,\56?/]{8,20}$"

# 响应

RESPONSE_STATUS = 'succeed'
RESPONSE_DATA = 'data'
COOKIE_ICON = 'icon'
SESSION_UID = 'index'
COOKEY_UID = 'k'
