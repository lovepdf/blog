# coding=utf-8
from django.conf.urls import patterns,url,include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list)
)


