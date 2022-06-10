from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader 
from django import forms

#登出功能
def Logout(request):
    #删除session
    if 'user_name' in request.session:
        del request.session['user_name']
    request.session.flush()
    
    #重定向到登陆界面
    response = HttpResponseRedirect('/user/login')

    #删除cookie
    if 'user_name' in request.COOKIES:
        response.delete_cookie('user_name')
    return response