from distutils.log import error
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader 
from django import forms

from django.contrib.auth.hashers import make_password, check_password

from user.models import *
from user.user_forms import *
from user.decoration import *

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
