from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader 
def test_url(request):
    return render(request,'test.html')
def create(request):
    return render(request,'article/create.html')