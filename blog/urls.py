# coding=utf-8
from django.conf.urls import patterns,url,include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list),   # 首页
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),  # 文章详情页
    url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
)


