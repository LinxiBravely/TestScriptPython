# coding=utf-8
#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
def hello(request):
    if request.method == 'GET':
        context = {}
        context['hello'] = 'Hello World GET!'
        return render(request, 'hello.html', context)
        # return HttpResponse("Hello world ! ")
    elif request.method == 'POST':
        context = {}
        context['hello'] = 'Hello World POST!'
        return render(request, 'hello.html', context)

def base(request):
    return(request,'base.html')


def index(request):
    return(request,'index.html')

def helloTest(request):
    context = {}
    context['hello'] = 'Hello World !'
    return(request,'helloTest.html',context)

# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将 session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or passworderror!'})

    else:
        return render(request,'index.html', {'error': 'username or passworderror!'})


# 发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器 cookie
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, "event_manage.html", {"user": username})
