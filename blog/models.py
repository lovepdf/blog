# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User)   # 作者信息
    title = models.CharField(max_length=200)   # 标题
    text = models.TextField()  # 文章内容
    created_date = models.DateTimeField(default=timezone.now)  # 创建时间
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''
        用于保存发布
        '''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title