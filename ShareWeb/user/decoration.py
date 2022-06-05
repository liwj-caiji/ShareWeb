from django.shortcuts import render, redirect
from django.urls import reverse


#检查登录情况装饰器,未登录则重定向到登录页面
def check_login(func):
    def fun( request, *args, **kwargs):
        user_name = request.session.get("user_name")
        if user_name:
            return func( request, *args, **kwargs)
        else:
            return redirect(reverse("user_login"))
    return fun

def check_login_modify(func):
    def fun( request, article_author, article_title, *args, **kwargs):
        user_name = request.session.get("user_name")
        if user_name == article_author:
            return func( request,article_author, article_title, *args, **kwargs)
        else:
            print('redirect')
            return redirect(reverse("user_login"))
    return fun
