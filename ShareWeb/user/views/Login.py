from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader 
from django import forms

from django.contrib.auth.hashers import make_password, check_password
from rsa import encrypt

from .. import models

class Login_Form(forms.Form):
    user_name = forms.CharField(label="用户名", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户名"}))
    user_account = forms.CharField(label="用户账号", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户账号"}))
    password = forms.CharField(label="密码", min_length=6, max_length=10,widget=forms.TextInput(attrs={'placeholder':"密码",'type':"password"}))
    remeber = forms.BooleanField(required=None)

def Login(request):

    #当第一次访问时,method为GET
    if (request.method) == 'GET':
        #如果不是第一次登录，在服务器端session有记录
        #重定向
        if 'user_name' in request.session:
            return render(request,"test.html")
        #检查cookie
        if 'user_name' in request.COOKIES:
            request.session['user_name'] = request.COOKIES['user_name']
            return render(request,"test.html")
        form = Login_Form()
        return render(request, "user/user_login.html", locals())

    elif(request.method) == 'POST':
        form = Login_Form(request.POST)
        
        if not form.is_valid():
            return HttpResponse("提交的信息有误")

        cur_user_account = form.cleaned_data['user_account']
        cur_raw_password = form.cleaned_data['password']
        cur_user = models.My_User.objects.filter(user_account=cur_user_account)

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


        request.session['user_name'] = cur_user_name
        response = HttpResponseRedirect("/user/info")
        #getlist获取checkbox的内容
        #勾选了则可以获取到remeber的值为on
        if 'on' in request.POST.getlist('remeber'):
            response.set_cookie('user_name',cur_user_name,60*60)
    
        return response