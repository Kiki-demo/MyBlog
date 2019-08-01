# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name=u'邮箱', unique=True)
    # 需要邮箱认证后才能激活，才能有权限评论等操作
    is_active = models.BooleanField(verbose_name=u'激活状态', default=False)
    picture = models.ImageField(verbose_name=u'头像', upload_to='pictures/', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        pass

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_to_user(self):
        # 具体发送邮件的逻辑可以自行查找实现，邮箱验证的时候需要用到
        pass

    def message_to_user(self):
        # 具体发送短信逻辑可以自行查找实现
        pass
