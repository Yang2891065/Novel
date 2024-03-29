from django.db import models

from book.models import Book


# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=11, verbose_name='用户名', primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    email = models.EmailField(verbose_name="邮箱")
    password = models.CharField(max_length=64, verbose_name='密码')
    sign = models.CharField(max_length=50, verbose_name='个人签名', null=True)
    info = models.CharField(max_length=150, verbose_name='个人描述', null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True)
    birthday = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'user_profile'


class Message(models.Model):
    user = models.ForeignKey(UserProfile)
    mark = models.ForeignKey(Book)
    time = models.DateTimeField(verbose_name='留言时间', auto_now_add=True)
