#!/usr/bin/python
from django.conf.urls import url, include
from django. contrib import admin
import ywy
from lll import views

urlpatterns = [
    url(r'^$', views.Loginpage),
    url(r'^Login/', views.Login, name="toLogin"),



]
# -*- coding:utf-8 -*-