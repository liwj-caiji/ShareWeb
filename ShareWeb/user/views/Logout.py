from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader 
from django import forms

#登出功能
def Logout(request):
    # print("进来")
    #删除session
    # print(request.session)
    if 'user_name' in request.session:
        # print('???')
        del request.session['user_name']
    request.session.flush()
    # print(request.session)
    response = HttpResponseRedirect('/user/login')
    #删除cookie
    if 'user_name' in request.COOKIES:
        # print("!!!")
        response.delete_cookie('user_name')
    return response