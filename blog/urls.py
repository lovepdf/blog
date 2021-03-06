# coding=utf-8
from django.conf.urls import patterns,url,include
from . import views

urlpatterns = [
    url(r'^$', views.post_list),   # 首页
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),  # 文章详情页
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),  # 编辑按钮
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),   # 草稿向
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),  # 发布功能
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),  # 删除功能
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),  # 用户登录

    ]


