# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-20 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190815_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcontent',
            name='book',
        ),
        migrations.AlterField(
            model_name='message',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookContent',
        ),
    ]
