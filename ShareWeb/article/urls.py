from ast import Delete
from django.urls import path,include
from django.conf.urls.static import static

from .views import test,Create,List,Search,Read,Modify

urlpatterns = [
    path('',test.test_url,name="test"),
    path('create/',Create.article_Create,name="article_create"),
    path('list/<str:article_author>/',List.article_List,name="article_list"),
    path('search/',Search.article_Search,name="article_search"),
    path('read/<str:article_author>/<str:article_title>/',Read.article_Read,name="article_read"),
    path('modify/<str:article_author>/<str:article_title>/',Modify.article_Modify,name="article_modify"),
]