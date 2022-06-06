from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 
from django import forms

from user.decoration import *
from user.models import *
# Create your views here.
# def user_info_html(request):
#     temp = loader.get_template('user_info.html')
#     html = temp.render({'name':'lwj'})
#     return HttpResponse(html)

@check_login
def Info(request):
    cur_user_name = request.session['user_name']
    try:
        cur_user = My_User.objects.get(user_name=cur_user_name)
        cur_user_account = cur_user.user_account
        return render(request,'user/user_info.html',locals()) 
    except Exception as e:
        return HttpResponse("当前用户信息不存在")
    

def test_url(request):
    return render(request,'test.html')


#表单
# class Login_Form(forms.Form):
#     user_name = forms.CharField(label="用户名", min_length=3, max_length=10)
#     user_account = forms.CharField(label="用户账号", min_length=3, max_length=10)
#     password = forms.CharField(label="密码", min_length=6, max_length=10)

# def Login(request):
#     if(request.method) == "POST":
#         form = Login_Form(request.POST)
#         if form.is_valid():
#             return HttpResponse("嘿嘿嘿")
#     else:
#         form = Login_Form()
#         #remeber = "<p>记住用户名: <input type=\"checkbox\" name=\"isSaved\"></p>"
#     return render(request, "user/user_login.html", locals())