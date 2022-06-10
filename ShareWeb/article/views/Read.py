from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader 
from django.urls import reverse

from article.models import *

#接收两个参数来唯一确定访问的article
def article_Read(request, article_author, article_title):
    #filter方法在不存在对象时返回空列表,不抛出异常
    article_list = My_Article.objects.filter(title=article_title,author_name=article_author)
    if not article_list:
        return HttpResponse("当前文章不存在")
    article = article_list[0]
    return render(request,'article/read.html',locals())