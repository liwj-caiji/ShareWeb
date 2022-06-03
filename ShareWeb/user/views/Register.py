from distutils.log import error
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader 
from django import forms

from django.contrib.auth.hashers import make_password, check_password
from rsa import encrypt

from user.models import *
from . import Login
from .. import user_forms


def Register(request):
    if request.method == "GET":
        form = user_forms.Register_Form()
        return render(request, "user/user_register.html", locals())
    elif request.method == "POST":
        form = user_forms.Register_Form(request.POST)
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
            old_user = My_User.objects.get( user_name = reg_user_name )
            error = "该用户名已注册"
            return render(request, "user/user_register.html", locals())
        except Exception as e:
            print("该用户名可用")
        try:
            old_user = My_User.objects.get( user_account = reg_user_account )
            error = "该账号已注册"
            return render(request, "user/user_register.html", locals())
        except Exception as e:
            new_user = My_User.objects.create( user_name = reg_user_name, user_account = reg_user_account, password = encrypt_password )
            form = user_forms.Login_Form()
            return redirect(reverse("user_login"))

        
