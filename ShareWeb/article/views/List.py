from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader 

from .. import models
from user.decoration import check_login

def article_List(request):
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