from django.db import models
from user.models import *

from django.utils import timezone
# Create your models here.
class My_Article(models.Model):
    #作者,ForeignKey用来指定多对一的一
    author = models.ForeignKey( My_User, on_delete=models.CASCADE)
    author_name = models.CharField( max_length=10, default="null")
    title  = models.CharField( max_length=30, unique=True)
    body   = models.TextField()
    created_time = models.DateTimeField( default=timezone.now )
    updated_time = models.DateTimeField( auto_now=True )

    class Meta:
        ordering = ['-created_time']
    
    def __str__(self):
        return self.title