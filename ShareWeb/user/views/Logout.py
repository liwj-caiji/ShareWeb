from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader 
from django import forms

#登出功能
def Logout(request):
    #删除session
    if 'username' in request.session:
        del request.session['username']
    request.session.flush()
    print(request.session)
    response = HttpResponseRedirect('/user/login')
    #删除cookie
    if 'username' in request.COOKIES:
        response.delete_cookie('username')
    return response