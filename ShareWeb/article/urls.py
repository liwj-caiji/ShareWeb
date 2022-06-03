from django.urls import path,include
from django.conf.urls.static import static

from .views import test,Create,List,Search,Read


urlpatterns = [
    path('',test.test_url,name="test"),
    path('create/',Create.article_Create,name="article_create"),
    path('list/',List.article_List,name="article_list"),
    path('search/',Search.article_Search,name="article_search"),
    path('read/',Read,name="article_read"),
]