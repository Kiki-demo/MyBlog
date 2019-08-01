# -*- coding: utf-8 -*-
"""
设置注册视图函数的 URL 模式
"""

from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
]
