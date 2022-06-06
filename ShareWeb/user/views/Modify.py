from distutils.log import error
from turtle import back
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader 
from django import forms

from django.contrib.auth.hashers import make_password, check_password
from numpy import delete

from user.models import *
from user.user_forms import *
from user.decoration import *

import os

@check_login
def Modify(request):
    if request.method == "GET":
        cur_user_name = request.session['user_name']
        cur_user = My_User.objects.get(user_name=cur_user_name)
        # print(cur_user)
        cur_user_account = cur_user.user_account
        form = Register_Form()
        value = { 'user_account':cur_user_account, 
                  'user_name':cur_user_name,
                  'form':form  }
        return render(request,'user/user_modify.html',context=value)
    elif request.method == "POST":
        cur_user_name = request.session['user_name']
        cur_user = My_User.objects.get(user_name=cur_user_name)
        old_password = request.POST['password']
        new_password = request.POST['password_new']
        if new_password and not old_password:
            return HttpResponse("修改密码需要输入原密码")
        if new_password and old_password:
            if check_password(old_password,cur_user.password):
                cur_user.password = make_password( new_password, None, 'pbkdf2_sha256' )
                cur_user.save()
            else:
                return HttpResponse("密码错误")
        new_user_name = request.POST['user_name']
        new_user_account = request.POST['user_account']

        print(cur_user)
        avatar_image = request.FILES.get('avatar_image')
        background_image = request.FILES.get('background_image')
        if avatar_image:
            avatar_image.name = cur_user.user_name + '-' + avatar_image.name
        if background_image:
            background_image.name = cur_user.user_name + '-' + background_image.name
        # avatart_save_name = cur_user_name + avatar_image.name
        # avatar_save_path = '%s/images/avatar/%s'(settings.MEDIA_ROOT, avatart_save_name)

        # background_save_name = cur_user_name + background_image.name
        # background_save_path = '%s/images/background/%s'(settings.MEDIA_ROOT, background_save_name)
        try:
            user_image = My_image.objects.get(user=cur_user)
            if avatar_image:
                delete_path = os.path.join(settings.MEDIA_ROOT) + user_image.avatar_image.url
                os.remove(delete_path)
                user_image.avatar_image = avatar_image
            if background_image:
                delete_path = os.path.join(settings.MEDIA_ROOT) + user_image.background_image.url
                os.remove(delete_path)
                user_image.background_image = background_image
            user_image.save()
            return HttpResponse("修改成功")
        except Exception as e:
            user_image = My_image.objects.create(avatar_image = avatar_image,background_image = background_image,user=cur_user)
            return HttpResponse("上传成功")
        return HttpResponse("结束")






