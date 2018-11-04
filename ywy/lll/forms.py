#!/usr/bin/python
from django import forms
from django.forms import widgets
from django.forms import fields
from django.core.exceptions import ValidationError
from .models import user
#
# class RegisterForm(forms.Form):
#
#     name = fields.CharField(error_messages={'required': '用户名不能为空.'},
#                                     widget=widgets.TextInput(),label="用户名"
#                                     )
#     pwd = fields.CharField(max_length=12, min_length=6,
#                                     error_messages={'required': '密码不能为空.',
#                                                     'min_length': '密码长度不能小于6',
#                                                     "max_length": '密码长度不能大于12'
#                                                     },
#                                     widget=widgets.PasswordInput(),
#                                     label="密码"
#                                     )
#     answer = fields.CharField(error_messages={'required': '密保答案不能为空'},
#                                   widget=widgets.TextInput(),label="密保答案"
#                                     )
#
#     def clean_name(self):
#         result = user.objects.filter(name=self.cleaned_data['name'])
#         if result:
#             raise ValidationError('该用户名已被使用')
#         return self.cleaned_data['name']

class ModelRegisterForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

        labels = {
            'answer': '密保答案',
            'name': '用户名',
            'pwd': '密码',
        }
        widgets = {
            'password': widgets.PasswordInput(),
        }

    def clean_name(self):
        result = user.objects.filter(name=self.cleaned_data['name'])
        if len(result) > 0:
            raise ValidationError('用户名重复')
        return self.cleaned_data['name']

    def clean_pwd(self):
        pwd=self.cleaned_data['pwd']
        if len(pwd) < 6:
            raise ValidationError('密码长度太短')
        elif len(pwd) > 20:
            raise ValidationError('密码长度太长')
        return self.cleaned_data['pwd']

class ModelLoginForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        labels = {
            'name': '用户名',
            'pwd': '密码',
            'answer': '密保答案'
        }
        widgets = {
            'password': widgets.PasswordInput(),
        }


    def clean_pwd(self):
        name = user.objects.filter(name=self.cleaned_data['name'])
        pwd = user.objects.filter(pwd=self.cleaned_data['pwd'])
        if len(name)and len(name) == 0:
            raise ValidationError("账号或密码错误")
        return self.cleaned_data['pwd']

 class changeForm(forms.ModelForm):
     class Meta:
         model = user
         fields = '__all__'
         labels = {
             'name': '用户名',
             'pwd': '密码',
             'answer': '密保答案'
         }

    def clean_pwd(self):
        name = self.cleaned_data['name']
        pwd = self.cleaned_data['pwd']
        if not user.objects.filter(pwd=pwd,name=name):
            raise ValidationError("原密码错误")
        return self.cleaned_data['pwd']

    def clean_newpwd(self):
        pwd = self.cleaned_data['pwd']
        if len(pwd) < 6:
            raise ValidationError('密码长度至少为6位')
        elif len(pwd) > 20:
            raise ValidationError('密码长度至多为20位')
        return self.cleaned_data['pwd']


# -*- coding:utf-8 -*-