from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader 
from django.urls import reverse


from article.models import *
from .. import article_forms

def article_Search(request):
    if  request.method == "GET":
        form = article_forms.Article_Search_Form()
        return render(request,"article/search.html",locals())
    elif request.method == "POST":
        form = article_forms.Article_Search_Form(request.POST)
        if not form.is_valid():
            error = "输入的信息有误"
            return render(request, "article/search.html",locals())
        search_type = form.cleaned_data['search_type']
        search_content = form.cleaned_data['search_content']
        if search_type == "article_title":
            search_result_list = My_Article.objects.filter(title__icontains=search_content)
            return render(request, 'article/search.html', locals())
        elif search_type == "article_author":
            search_result_list = My_Article.objects.filter(author_name=search_content)
        print(form.cleaned_data)
        return render(request, 'article/search.html', locals())
    return HttpResponse("页面出错")