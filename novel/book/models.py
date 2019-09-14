from django.db import models


# Create your models here.
class Book(models.Model):
    bookName = models.CharField(verbose_name='书名', max_length=50)
    author = models.CharField(verbose_name='作者', max_length=50)
    bookInfo = models.TextField(verbose_name='内容简介', max_length=90)
    bookState = models.CharField(verbose_name='状态', max_length=10, default='null')
    bookLog = models.ImageField(upload_to=None, max_length=100)
    kind = models.CharField(verbose_name='属', max_length=100, default='null')


class BookContent(models.Model):
    book = models.ForeignKey(Book)
    menu = models.CharField(verbose_name='章节名', max_length=100)
    content = models.TextField(verbose_name='内容')
