# Generated by Django 3.2.13 on 2022-06-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_article',
            name='author_name',
            field=models.CharField(default='null', max_length=10),
        ),
    ]
