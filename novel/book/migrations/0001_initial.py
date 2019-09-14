# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-20 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50, verbose_name='书名')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('info', models.TextField(max_length=90, verbose_name='内容简介')),
                ('state', models.CharField(default='null', max_length=10, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='BookContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=100, verbose_name='章节名')),
                ('content', models.TextField(max_length=4000, verbose_name='内容')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
    ]
