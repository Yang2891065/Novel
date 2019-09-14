import hashlib
import json

from django.http import JsonResponse
from django.shortcuts import render

# 注册界面(账户名、密码*2)
from book.models import Book
from btoken.views import make_token
from tools.login_check import login_check
from user.models import UserProfile


# Create your views here.


def register_view(request):
    return render(request, "register.html", locals())


# 登录界面(账户名、密码(保存当前用户，保存当前密码))
def login_view(request):
    return render(request, "login.html", locals())


@login_check('PUT')
def users(request, username=None):
    if request.method == 'POST':
        # 注册
        json_str = request.body
        if not json_str:
            result = {'code': 202, 'error': 'Please POST data!!'}
            return JsonResponse(result)
        # 如果当前报错,请执行 json_str = json_str.decode()
        json_obj = json.loads(json_str)

        username = json_obj.get('username')
        email = json_obj.get('email')
        password_1 = json_obj.get('password_1')
        password_2 = json_obj.get('password_2')

        if not username:
            result = {'code': 203, 'error': 'Please give me username !'}
            return JsonResponse(result)

        if not email:
            result = {'code': 204, 'error': 'Please give me email !'}
            return JsonResponse(result)

        if not password_1 or not password_2:
            result = {'code': 205, 'error': 'Please give me password !'}
            return JsonResponse(result)

        if password_1 != password_2:
            result = {'code': 206, 'error': 'Please give me right password !'}
            return JsonResponse(result)

        # 检查用户名是否存在
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 207, 'error': 'The username is used !!! '}
            return JsonResponse(result)

        # 密码散列
        p_m = hashlib.sha256()
        p_m.update(password_1.encode())

        try:
            UserProfile.objects.create(username=username, nickname=username, email=email, password=p_m.hexdigest())
        except Exception as e:
            print('----create error is %s' % (e))
            result = {'code': 500, 'error': 'Sorry, server is busy !'}
            return JsonResponse(result)

        token = make_token(username)
        # token 编码问题 !!!! bytes串不能json dumps, 所以要执行decode方法
        result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
        # http://127.0.0.1:5000/register
        rep = JsonResponse(result)
        rep.set_cookie(username, value=token)
        request.session[username] = token.decode()
        return rep

    elif request.method == 'GET':
        # 获取数据
        if username:
            # 获取指定用户数据
            users = UserProfile.objects.filter(username=username)
            if not users:
                # 当前username的用户不存在
                result = {'code': 208, 'error': 'The user is not existed'}
                return JsonResponse(result)
            user = users[0]
            if request.GET.keys():
                # 当前请求有查询字符串
                data = {}
                for key in request.GET.keys():
                    if key == 'password':
                        # 如果查询密码,则continue!
                        continue
                    # hasattr 第一个参数为对象, 第二个参数为 属性字符串 ->  若对象含有第二个参数的属性,则返回True,反之 False
                    # getattr 参数同hasattr, 若对象含有第二个参数的属性,则返回对应属性的值, 反之 抛出异常 AttributeError
                    if hasattr(user, key):
                        if key == 'avatar':
                            # avatar属性需要调用str方法 __str__
                            data[key] = str(getattr(user, key))
                        else:
                            data[key] = getattr(user, key)
                result = {'code': 200, 'username': username, 'data': data}
            else:
                # 无查询字符串,即获取指定用户数据
                result = {'code': 200, 'username': username,
                          'data': {'info': user.info, 'sign': user.sign, 'nickname': user.nickname,
                                   'avatar': str(user.avatar)}}

            return JsonResponse(result)
        else:
            # 没有username
            # [{username nickname sign info email avatar}]
            all_users = UserProfile.objects.all()
            result = []
            for _user in all_users:
                d = {}
                d['username'] = _user.username
                d['nickname'] = _user.nickname
                d['sign'] = _user.sign
                d['info'] = _user.info
                d['email'] = _user.email
                d['avatar'] = str(_user.avatar)
                result.append(d)
            return JsonResponse({'code': 200, 'data': result})


def leader_view(request):
    return render(request, "leader.html", locals())


def vip(request, vip_name):
    books = Book.objects.all()
    user = vip_name
    return render(request, "vip.html", locals())


def kind(request, vip_name, kind_name):
    books = Book.objects.filter(kind=kind_name)
    user = vip_name
    return render(request, "vip.html", locals())


def answer(request, vip_name):
    return render(request, 'Sorry.html', locals())
