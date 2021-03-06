# Generated by Django 3.2.13 on 2022-06-01 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='my_user',
            name='password',
            field=models.CharField(max_length=10, verbose_name='密码'),
        ),
    ]
