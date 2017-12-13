from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User


# Create your views here.


def to_sign_in(req):
    try:
        username = req.COOKIES.get('username')
        password = req.COOKIES.get('password')
        if User.objects.filter(username=username)[0].password == password:
            return HttpResponseRedirect(reverse('movie:home'))
        else:
            raise KeyError
    except:
        return render(req, 'sign_in.html')


def to_sign_up(req):
    return render(req, 'sign_up.html')


def sign_up(req):
    user = User()
    name = req.POST['username']
    passwd1 = req.POST['password1']
    passwd2 = req.POST['password2']
    if User.objects.filter(username=name):
        return render(req, 'sign_up.html')
    elif passwd2 == passwd1:
        user.username = name
        user.password = passwd1
        user.save()
        return HttpResponse('成功')
    else:
        return render(req, 'sign_up.html')

def sign_in(req):
    name = req.POST['username']
    password = req.POST['password']
    user = User.objects.filter(username=name)
    if user:
        if user[0].password == password:
            response = HttpResponseRedirect(reverse('movie:home'))
            try:
                if req.POST['remeber'][0]:
                    response.set_cookie('username', name)
                    response.set_cookie('password', password)
                else:
                    raise KeyError
            except:
                pass
            finally:
                return response
        else:
            return HttpResponse('密码错误')
    else:
        return HttpResponse('用户名不存在')
