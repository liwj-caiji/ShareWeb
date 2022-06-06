from django.contrib import admin
from user.models import My_User,My_image
# Register your models here.
admin.site.register([My_User,My_image])
