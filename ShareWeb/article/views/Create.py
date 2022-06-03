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
        new_article_title = request.POST.get('title')
        new_article_body = request.POST.get('body')
        cur_user_name =  request.session.get("user_name")
        cur_user = My_User.objects.filter(user_name=cur_user_name)
        if not cur_user:
            return HttpResponse("当前登录信息有误")
        My_Article.objects.create( title=new_article_title, body=new_article_body, author_name=cur_user_name, author=cur_user[0])
        return redirect(reverse("article_list"))
    # 如果用户请求获取数据
    else:
        form = article_forms.Article_Create_Form()
        #print(request.session['user_name'])
        return render(request, 'article/create.html', locals())