from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader
from django.urls import reverse

from user.models import *
from article.models import *
from user.decoration import check_login
from article import article_forms

@check_login
def article_Create(request):
    if request.method == 'POST':

        #从表单中获取对应的信息
        new_article_title = request.POST.get('title')
        new_article_body = request.POST.get('body')

        #从session中获取用户名,获取对应用户信息
        cur_user_name =  request.session.get("user_name")
        cur_user = My_User.objects.filter(user_name=cur_user_name)

        #用户不存在
        if not cur_user:
            return HttpResponse("当前登录信息有误")
        
        #创建My_Article对象,与对应用户关联
        My_Article.objects.create( title=new_article_title, body=new_article_body, author_name=cur_user_name, author=cur_user[0])
        
        #重定向到article的list页面,reverse使用kwargs传递参数
        return redirect(reverse("article_list",kwargs={'article_author':cur_user_name}))
    # 如果用户请求获取数据
    else:
        #GET方法返回一个空表单
        form = article_forms.Article_Create_Form()
        #print(request.session['user_name'])
        return render(request, 'article/create.html', locals())