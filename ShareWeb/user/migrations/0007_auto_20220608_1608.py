# Generated by Django 3.2.13 on 2022-06-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_avatar_imge_my_image_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_image',
            name='avatar_image',
            field=models.ImageField(default='images/icon/logo1.png', upload_to='images/avatar'),
        ),
        migrations.AlterField(
            model_name='my_image',
            name='background_image',
            field=models.ImageField(default='images/icon/logo2.png', upload_to='images/background'),
        ),
    ]