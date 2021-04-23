#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""URL配置

`urlpatterns`列表将URL路由到视图。有关更多信息，请参阅：https://docs.djangoproject.com/en/3.1/topics/http/url/

示例：
函数视图
    1. 添加导入：从my_app导入视图
    2. 将URL添加到urlpatterns：path('', views.home, name='home')

基于类的视图
    1. 添加导入：从其他_应用程序视图导入主页
    2. 将URL添加到urlpatterns：path('blog/', include('blog.urls'))

引用另一个URLconf
    1. 导入include()函数：从django.url导入include、path
    2. 将URL添加到urlpatterns：path('blog/', include('blog.urls'))
"""
from Demo.view import *
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('signUp', sign_up),
    path('signIn', sign_in),
    path('getAll', get_users),
    path('delete', delete_user),
]
re_path('', index)
