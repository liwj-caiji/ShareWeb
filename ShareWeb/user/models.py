from django.db import models

# Create your models here.
class My_User(models.Model):
    user_name = models.CharField( max_length=10, unique=True, verbose_name='用户名')
    user_account = models.CharField( max_length=10, unique=True, verbose_name='用户账号')
    password = models.CharField(max_length=10, verbose_name='密码')
    create_time=models.DateTimeField(auto_now_add=True)#第一次创建的时间
    def __str__(self):
        return self.user_name