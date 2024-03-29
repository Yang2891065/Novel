# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-15 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190807_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcase',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookcase',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='bookcase',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='state',
            field=models.CharField(default='null', max_length=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='info',
            field=models.TextField(max_length=90, verbose_name='内容简介'),
        ),
        migrations.AlterField(
            model_name='bookcontent',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Book'),
        ),
        migrations.AlterField(
            model_name='bookcontent',
            name='content',
            field=models.TextField(max_length=4000, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='message',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Book'),
        ),
        migrations.DeleteModel(
            name='BookCase',
        ),
    ]
