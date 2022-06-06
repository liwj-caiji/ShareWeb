from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader
from django.urls import reverse


from user.models import *
from article.models import *
from article.article_forms import *
from user.decoration import *


@check_login_modify
def article_Modify(request, article_author, article_title):
    if request.method == "GET":
        article_list = My_Article.objects.filter(title=article_title,author_name=article_author)
        if not article_list:
            return HttpResponse("打开失败")
        article = article_list[0]
        print(article)
        return render(request,'article/modify.html',locals())
    elif request.method == "POST":
        error = ""
        to_delete = request.POST.getlist("to_delete")
        print(to_delete)
        if not to_delete:
            print("here")
            try:
                article = My_Article.objects.get(title=article_title,author_name=article_author)
                new_article_title = request.POST.get("title")
                print(new_article_title)
                new_article_body  = request.POST.get("body")
                print(new_article_body)
                article.title = new_article_title
                article.body  = new_article_body
                error = "标题重复"
            #如果下面抛出异常,则说明保存失败,要保存的标题重复
                article.save()
                return redirect(reverse('article_list'))
            except Exception as e:
                if not error:
                    return HttpResponse("修改失败")  
                else:
                    return HttpResponse(error)
        else:
            try:
                error = "文章不存在"
                article = My_Article.objects.get(title=article_title,author_name=article_author)
                error = "删除失败"
                article.delete()
                return redirect(reverse('article_list'))
            except Exception as e:
                return HttpResponse(error)
        
        