from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader 

from .. import models
from user.decoration import check_login
from article import article_forms

@check_login
def article_Create(request):
    if request.method == 'POST':
        new_article_title = request.POST.get('title')
        new_article_body = request.POST.get('body')
        cur_user_name =  request.session.get("user_name")
        models.My_Article.objects.create( title=new_article_title, body=new_article_body)
        return redirect("article:article_list")
    # 如果用户请求获取数据
    else:
        form = article_forms.Article_Create_Form()
        print(request.session['user_name'])
        return render(request, 'article/create.html', locals())