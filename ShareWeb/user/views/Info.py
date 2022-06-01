from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 
from django import forms
# Create your views here.
# def user_info_html(request):
#     temp = loader.get_template('user_info.html')
#     html = temp.render({'name':'lwj'})
#     return HttpResponse(html)

def Info(request):
    user_name = ''
    user_account = ''
    password = ''
    return render(request,'user/user_info.html',locals())

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