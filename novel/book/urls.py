from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload', views.book_upload),
    url(r'^write', views.write_sql),
    url(r'^chapter', views.chapter_view),
    # url(r'^page/$', views.page_view),
    # url(r'^(?P<book_name>[\w]+)/(?P<booK_chapter>[\w]+)$', views.view_test),
    url(r'^(?P<book_name>[\w]+)/(?P<book_chapter>.+)/ready$', views.content_view)
]
