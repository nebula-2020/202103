#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
项目的WSGI配置。

它将WSGI callable公开为名为``application``的模块级变量。

有关此文件的详细信息，请参阅：https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Demo.settings')

application = get_wsgi_application()
