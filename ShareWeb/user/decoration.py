from django.shortcuts import redirect, render
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