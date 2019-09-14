from django.conf.urls import url

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/user/register/
    url(r'^register$', views.register_view),
    # http://127.0.0.1:8000/user/login
    url(r'^login$', views.login_view),
    url(r'^leader$', views.leader_view),
    # http://127.0.0.1:8000/users
    url(r'^users$', views.users, name='users'),
    # http://127.0.0.1:8000/users/<username>
    url(r'^(?P<username>[\w]+)$', views.users),
    # http://127.0.0.1:8000/vip/user(?)
    url(r'^vip/(?P<vip_name>[\w]+)$', views.vip),
    url(r'^vip/(?P<vip_name>[\w]+)/(?P<kind_name>[\w][\w])$', views.kind),
    url(r'vip/(?P<vip_name>[\w]+)/[\w]+', views.answer)

]
