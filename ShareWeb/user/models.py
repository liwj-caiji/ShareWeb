from distutils.command import upload
from django.db import models

# Create your models here.
class My_User(models.Model):
    user_name = models.CharField( max_length=10, unique=True, verbose_name='用户名')
    user_account = models.CharField( max_length=10, unique=True, verbose_name='用户账号')
    password = models.CharField( max_length=100, verbose_name='密码')
    create_time  = models.DateTimeField( auto_now_add=True)#第一次创建的时间
    def __str__(self):
        return self.user_name

class My_image(models.Model):
    avatar_image = models.ImageField(upload_to="images/avatar" ,default="images/icon/logo1.png")
    background_image = models.ImageField(upload_to="images/background" ,default="images/icon/logo2.png")
    #用户与图片信息一一对应
    user = models.OneToOneField( My_User, on_delete=models.CASCADE)