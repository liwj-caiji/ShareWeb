from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage,InvalidPage

from article.models import My_Article
from user.decoration import check_login

def article_List(request, article_author):
    if request.method == "GET":
        article_list = My_Article.objects.filter(author_name=article_author)
        print(article_list)
        if not article_list:
           return HttpResponse("该用户不存在或该用户未发表任何文章")
        article_paginator =  Paginator(article_list, 4)
        try:
            page_index = request.GET.get('page',1)
            print(page_index)
            page = article_paginator.page(int(page_index)) 
            print(page)
            return render(request,'article/list.html',locals())
        except Exception as e:
            return HttpResponse("页面打开失败")
        
    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    # if request.GET.get('order') == 'total_views':
    #     article_list = ArticlePost.objects.all().order_by('-total_views')
    #     order = 'total_views'
    # else:
    #     article_list = ArticlePost.objects.all()
    #     order = 'normal'

    # paginator = Paginator(article_list, 4)
    # page = request.GET.get('page')
    # articles = paginator.get_page(page)
    # context = { 'articles': articles, 'order': order }

    # return render(request, 'article/list.html', context)
    return HttpResponse("成功")