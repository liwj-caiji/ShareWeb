from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader 
from django.urls import reverse

from django.contrib.auth.hashers import check_password

from user.models import *
from .. import user_forms



def Login(request):
    #当第一次访问时,method为GET
    if (request.method) == 'GET':
        #如果不是第一次登录，在服务器端session有记录
        #重定向
        if 'user_name' in request.session:
            return redirect(reverse('user_info'))
        #检查cookie
        if 'user_name' in request.COOKIES:
            request.session['user_name'] = request.COOKIES['user_name']
            return redirect(reverse('user_info'))
        form = user_forms.Login_Form()
        return render(request, "user/user_login.html", locals())

    elif(request.method) == 'POST':
        form = user_forms.Login_Form(request.POST)
        
        if not form.is_valid():
            return HttpResponse("提交的信息有误")

        cur_user_account = form.cleaned_data['user_account']
        cur_raw_password = form.cleaned_data['password']
        cur_user = My_User.objects.filter(user_account=cur_user_account)

        if not cur_user:
            error = '当前用户不存在或密码错误'
            return render(request,'user/user_login.html', locals())
        
        #只有一个匹配用户
        cur_user = cur_user[0]
        cur_user_name = cur_user.user_name
        encrypt_password = cur_user.password
        if not check_password(cur_raw_password,encrypt_password):
            error = '当前用户不存在或密码错误'
            return render(request,'user/user_login.html', locals())
        
        # response = HttpResponseRedirect("/user/info")
        #getlist获取checkbox的内容
        #勾选了则可以获取到remeber的值为on
        if 'on' in request.POST.getlist('remeber'):
            request.set_cookie('user_name',cur_user_name,60*60)
            
        print(request.COOKIES.get('user_name'))
        request.session['user_name'] = cur_user_name
    
        return redirect(reverse('user_info'))

