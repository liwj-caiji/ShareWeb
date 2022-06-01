from distutils.log import error
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader 
from django import forms

from django.contrib.auth.hashers import make_password, check_password
from rsa import encrypt

from .. import models

class Register_Form(forms.Form):
    user_name = forms.CharField(label="用户名", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户名"}))
    user_account = forms.CharField(label="用户账号", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户账号"}))
    password = forms.CharField(label="密码", min_length = 6, max_length=20,widget=forms.TextInput(attrs={'placeholder':"密码",'type':"password"}))
    password_confirm = forms.CharField(label="确认密码", min_length=6, max_length=10,widget=forms.TextInput(attrs={'placeholder':"确认密码",'type':"password"}))

def Register(request):
    if request.method == "GET":
        form = Register_Form()
        return render(request, "user/user_register.html", locals())
    elif request.method == "POST":
        form = Register_Form(request.POST)
        if not form.is_valid():
            error = "输入的信息有误"
            return render(request, "user/user_register.html", locals())
        
        reg_user_name = form.cleaned_data['user_name']
        reg_user_account = form.cleaned_data['user_account']
        reg_password = form.cleaned_data['password']
        reg_password_confirm = form.cleaned_data['password_confirm']

        if reg_password != reg_password_confirm:
            error = "两次密码不一致"
            return render(request, "user/user_register.html", locals())
        encrypt_password = make_password( reg_password, None, 'pbkdf2_sha256' )
        print(encrypt_password)
        try:
            old_user = models.My_User.objects.get( user_name = reg_user_name )
            error = "该用户名已注册"
            return render(request, "user/user_register.html", locals())
        except Exception as e:
            print("该用户名可用")
        try:
            old_user = models.My_User.objects.get( user_account = reg_user_account )
            error = "该账号已注册"
            return render(request, "user/user_register.html", locals())
        except Exception as e:
            new_user = models.My_User.objects.create( user_name = reg_user_name, user_account = reg_user_account, password = encrypt_password )
            return render(request, "user/user_login.html" )

        
