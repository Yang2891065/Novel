import os
import re

from django.http import JsonResponse
from django.shortcuts import render

from book.models import Book, BookContent
from tools.right_check import right_check


# Create your views here.


def book_upload(request):
    return render(request, 'upload.html')


def write_sql(request):
    if not request.method == 'POST':
        result = {'code': 102, 'error': 'Please use POST !'}
        return JsonResponse(result)
    book_name = request.POST.get('book_name')
    author = request.POST.get('author')
    book_info = request.POST.get('book_info')
    book_kind = request.POST.get('book_kind')
    book_state = request.POST.get('book_state')
    book_log = request.FILES.get('book_log')
    book_content = request.FILES.get('book_content')
    tail = str(book_log)
    tail = tail.split('.')[-1]
    up = os.getenv("HOME")
    with open(up + '/novel/static/fictionImages/' + book_name + '.' + tail, 'wb') as f1:
        while True:
            data = book_log.read(1024)
            if not data:
                break
            f1.write(data)

    book_log = '../static/fictionImages/' + book_name + '.' + tail
    books = Book.objects.create(bookName=book_name, author=author, bookInfo=book_info,
                                bookLog=book_log, bookState=book_state, kind=book_kind)

    chapter_dic = {}
    chapter_list = []
    chapter = -1
    for lin in book_content:
        lin = lin.decode()
        data = re.findall(r'^第.{1,5}[回章节]', lin)
        print(data, end=' ')
        if "-" in lin.strip() or "" == lin.strip():
            continue
        if data:
            chapter_list.append(lin.strip().replace(' ', ''))
            chapter += 1
            chapter_dic[chapter_list[chapter]] = ''

        else:
            chapter_dic[chapter_list[chapter]] += lin
    count = 0
    for key, value in chapter_dic.items():
        BookContent.objects.create(menu=key, content=value, book=books)
        count += 1
    result = {'code': 200}
    return JsonResponse(result)


@right_check
def chapter_view(request):
    title = request.POST.get('bookName')
    user = request.POST.get('user')
    session = request.session.get(user, None)
    cookie = request.COOKIES[user]
    id = Book.objects.filter(bookName=title)
    books = BookContent.objects.filter(book_id=id)
    book_list = []
    data = []
    count = 0
    for i in books:
        if count == 5:
            count = 0
            book_list.append(data)
            data = []
        count += 1
        data.append(i.menu)
    return render(request, "chapter.html", locals())


@right_check
def content_view(request, **kwargs):
    user = request.POST.get('user')
    book = kwargs['book_name']
    chapter = kwargs['book_chapter']

    book_content = BookContent.objects.filter(menu=chapter)

    for i in book_content:
        title = i.menu

    return render(request, 'content.html', locals())


# 观看的章节(章节名、更新时间、小说内容、留言评论)
def page_view(request):
    jojo = "book/page"
    return render(request, "temp.html", locals())
