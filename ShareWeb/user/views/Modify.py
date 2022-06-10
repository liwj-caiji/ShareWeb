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
    #根据request的session获取用户名
        cur_user_name = request.session['user_name']

    #获取对应的用户信息,由于经过了装饰器的判定,因此该get方法没有try
        cur_user = My_User.objects.get(user_name=cur_user_name)

    #注册时每个用户设置了默认的My_image
        cur_user_images = My_image.objects.get(user=cur_user)
        cur_user_account = cur_user.user_account

    #返回表单,用户信息通过locals()形成的字典填充
        form = Register_Form()
        return render(request,'user/user_modify.html',locals())

    elif request.method == "POST":
        cur_user_name = request.session['user_name']
        cur_user = My_User.objects.get(user_name=cur_user_name)

    #获取表单中的密码信息
        old_password = request.POST['password']
        new_password = request.POST['password_new']
    
    #修改原密码需要输入原密码
        if new_password and not old_password:
            return HttpResponse("修改密码需要输入原密码")
    
    #修改密码时对密码进行验证
        if new_password and old_password:
        #验证通过
            if check_password(old_password,cur_user.password):
            #加密算法的选择与注册时一致
                cur_user.password = make_password( new_password, None, 'pbkdf2_sha256' )
            #调用save方法将修改写回数据库
                cur_user.save()
            else:
                return HttpResponse("密码错误")
    
    #获取表单中的信息
        new_user_name = request.POST['user_name']
        new_user_account = request.POST['user_account']

    #获取头像文件
        avatar_image = request.FILES.get('avatar_image')
        if avatar_image:
            avatar_image.name = cur_user.user_name + '-' + avatar_image.name
            
        # background_image = request.FILES.get('background_image')
        # if background_image:
        #     background_image.name = cur_user.user_name + '-' + background_image.name
        
        # avatart_save_name = cur_user_name + avatar_image.name
        # avatar_save_path = '%s/images/avatar/%s'(settings.MEDIA_ROOT, avatart_save_name)
        # background_save_name = cur_user_name + background_image.name
        # background_save_path = '%s/images/background/%s'(settings.MEDIA_ROOT, background_save_name)

        #获取用户的图片信息
        try:
            user_image = My_image.objects.get(user=cur_user)
            #如果用户已经有头像文件,则将之前的删除,保存新的
            
            if avatar_image :
                delete_path = os.path.join(settings.MEDIA_ROOT) + user_image.avatar_image.url
                print(user_image.avatar_image.url)
                #如果用户头像是默认头像则不删除
                if user_image.avatar_image.url == u'/images/icon/logo1.png':
                    pass
                else:
                    os.remove(delete_path)
                user_image.avatar_image = avatar_image

            # if background_image:
            #     delete_path = os.path.join(settings.MEDIA_ROOT) + user_image.background_image.url
            #     os.remove(delete_path)
            #     user_image.background_image = background_image

            #将保存的图片写回数据库
            user_image.save()
            print("修改用户信息成功")

            #重定向到用户信息界面
            return redirect(reverse('user_info'))

        except Exception as e:
            #如果用户不存在相联的My_image对象,即get方法抛出异常
            #则create对应的My_image对象
            user_image = My_image.objects.create(avatar_image = avatar_image,user=cur_user)
            return redirect(reverse('user_info'))





