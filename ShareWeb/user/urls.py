from django.urls import path,include
from django.conf.urls.static import static


from .views import Info,Login,Logout,Register


urlpatterns = [ 
    path('info/',Info.Info,name='user_info'),
    path('test/',Info.test_url,name='test'),
    path('login/',Login.Login,name='user_login'),
    path('logout/',Logout.Logout,name='user_logout'),
    path('register/',Register.Register,name='user_register'),
    path('article/',include('article.urls')),] 