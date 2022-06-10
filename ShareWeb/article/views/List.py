from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage,InvalidPage

from article.models import My_Article
from user.decoration import check_login

#接收一个参数author_name,列出该用户名对应用户的所有article
def article_List(request, article_author):
    #GET方法
    if request.method == "GET":
        #根据用户名获取对应的article组成的列表
        article_list = My_Article.objects.filter(author_name=article_author)
        
        #如果列表为空,返回错误信息
        if not article_list:
           return HttpResponse("该用户不存在或该用户未发表任何文章")
        
        #使用django内置的分页器,每页四个列表元素
        article_paginator =  Paginator(article_list, 4)
    
        try:
            #获取页面传递的page参数,用来控制对应的页,默认为1
            page_index = request.GET.get('page',1)

            #当page_index不合法时,下面会抛出异常
            page = article_paginator.page(int(page_index)) 

            #将局部变量通过locals()传递到模板
            return render(request,'article/list.html',locals())
        except Exception as e:
            return HttpResponse("页面打开失败")
            
    return HttpResponse("非GET方法")