#!/usr/bin/python
from django.conf.urls import url, include
from django. contrib import admin
import ywy
from lll import views

urlpatterns = [
    url(r'^$', views.Loginpage),
    url(r'^toLogin/', views.Login, name="toLogin"),
    url(r'^changePwd/', views.Changepage,name="changePwd"),
    url(r'^toChangePwd/', views.changePwd,name="toChangePwd"),

    url(r'^findPwd/', views.findPage, name="FindPwd"),
    url(r'^tofindPwd/', views.findPwd,name="toFindPwd"),

    url(r'^theRegister/', views.Registerpage, name="Register"),
    url(r'^toRegister/', views.Register, name="toRegister"),

    url(r'^newPwd/', views.setpwd, name="setNewpwd"),
    url(r'^toSet/', views.setPwd, name='toSetpwd'),

    url(r'^myBlog/', views.blog, name="putBlog")


]
# -*- coding:utf-8 -*-