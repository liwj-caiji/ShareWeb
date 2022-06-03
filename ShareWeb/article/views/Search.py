from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader 
from django.urls import reverse


from .. import models
from .. import article_forms

def article_Search(request):
    print("?")
    print(request.method)
    if (request.method) == "GET":
        form = article_forms.Article_Search_Form()
        return render(request,"article/search.html",locals())
    # else:
    #     form = article_forms.Article_Search_Form(request.POST)
    #     print("????")
    #     print(reverse("article_create"))
    #     print(form)
       
    #     return redirect(reverse("article_create"))
    print("?")
    print(request.method)
    return redirect(reverse("test"))
