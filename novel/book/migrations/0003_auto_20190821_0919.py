# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-21 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=None),
        ),
    ]
