from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader
from django.urls import reverse


from user.models import *
from article.models import *
from article.article_forms import *
from user.decoration import *

#检验登录
#接收两个参数,由于article_title不具有unique=True属性,因此还需要用户名来确定article对象
#用户仅能编辑自己的article
@check_login_modify
def article_Modify(request, article_author, article_title):

    if request.method == "GET":
        #获取列表,该列表若不为空则只有一个对象
        article_list = My_Article.objects.filter(title=article_title,author_name=article_author)
        if not article_list:
            return HttpResponse("打开失败")
        article = article_list[0]
        print(article)
        return render(request,'article/modify.html',locals())
    elif request.method == "POST":
        error = ""
        #判断用户是否选择了删除选项
        to_delete = request.POST.getlist("to_delete")
        #用户没选择删除
        if not to_delete:
            try:
                #更改对应article的信息
                article = My_Article.objects.get(title=article_title,author_name=article_author)
                new_article_title = request.POST.get("title")
                new_article_body  = request.POST.get("body")
                article.title = new_article_title
                article.body  = new_article_body
                error = "标题重复"
                #如果下面抛出异常,则说明保存失败,要保存的标题重复
                article.save()
            except Exception as e:
                if not error:
                    return HttpResponse("修改失败")  
                else:
                    return HttpResponse(error)
            else:
                #重定向
                url = reverse('article_list', kwargs={'article_author':article.author_name}) 
                return redirect(url)

        else:
            #删除对应article
            try:
                error = "文章不存在"
                article = My_Article.objects.get(title=article_title,author_name=article_author)
                error = "删除失败"
                article.delete()
                url = reverse('article_list', kwargs={'article_author':article.author_name})
                return redirect(url)
            except Exception as e:
                return HttpResponse(error)
        
        