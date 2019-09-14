import json

from django.http import HttpResponse


def right_check(fun):
    def wrapper(request, *args, **kwargs):
        user = request.POST.get('user')
        session = request.session.get(user, None)
        cookie = request.COOKIES.get(user, None)
        print(session)
        print(cookie)
        if not cookie:
            result = {"code": 304}
            result = json.dumps(result)
            return HttpResponse(result)

        if session == cookie:
            return fun(request, *args, **kwargs)

    return wrapper
