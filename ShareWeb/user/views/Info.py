from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 
from django import forms

from article.models import *
from user.decoration import *
from user.models import *
# Create your views here.
# def user_info_html(request):
#     temp = loader.get_template('user_info.html')
#     html = temp.render({'name':'lwj'})
#     return HttpResponse(html)

#查看用户信息需要登录
@check_login
def Info(request):
    #从session中获取用户名
    cur_user_name = request.session['user_name']
    try:
    #根据用户名获取用户信息
    #get失败会抛出异常
        cur_user = My_User.objects.get(user_name=cur_user_name)
        cur_user_account = cur_user.user_account
    #获取用户上传的图片
        cur_user_images_list = My_image.objects.filter(user=cur_user)
        if cur_user_images_list:
            cur_user_images = cur_user_images_list[0]
        else:
            cur_user_images = None
        cur_user_article_list = My_Article.objects.filter(author=cur_user)
        cur_user_article_list = cur_user_article_list[:3]
        # cur_user_images_background_url = settings.MEDIA_ROOT + cur_user_images.background_image.url
        # print(cur_user_images_background_url)
        print(cur_user_article_list)
        return render(request,'user/user_info.html',locals()) 
    except Exception as e:
        return HttpResponse("当前用户信息不存在")
    

def test_url(request):
    return render(request,'test.html')