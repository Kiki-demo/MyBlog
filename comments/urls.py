# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import post_comment

app_name = 'comments'
urlpatterns = [
    url(r'comment/post/(?P<post_pk>[0-9]+)/$', post_comment, name='post_comment')
]
