#!/usr/bin/python
from django.conf.urls import url, include
from django. contrib import admin
import ywy
from lll import views

urlpatterns = [
    url(r'^$', views.Loginpage),
    url(r'^Login/', views.Login,name="toLogin"),
    url(r'^changePwd/', views.Changepage,name="changePwd"),
    url(r'^toChangePwd/', views.changePwd,name="toChangePwd"),

    url(r'^findPwd/', views.findPage, name="FindPwd"),
    url(r'^tofindPwd/', views.findPwd,name="toFindPwd"),

    url(r'^theRegister/', views.Registerpage, name="Register"),
    url(r'^toRegister/', views.Register, name="toRegister"),


]
# -*- coding:utf-8 -*-