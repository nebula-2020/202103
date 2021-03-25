#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
项目的ASGI配置。

它将ASGI callable公开为名为``application``的模块级变量。

有关此文件的详细信息，请参阅：https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Demo.settings')

application = get_asgi_application()
