from django.shortcuts import render

from book.models import Book


# 主页(书名、简介、最后更新时间、是否完结)
def index_view(request):
    books = Book.objects.all()
    return render(request, "index.html", locals())
