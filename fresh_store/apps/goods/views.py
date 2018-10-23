from django.shortcuts import render
from django.http import HttpResponse
from ..user.models import *
import re
# Create your views here.

def login(request):
    return render(request,'goods/login.html')

def register(request):
    if request.method == 'GET':
        return render(request,'goods/register.html')
    else:
        username = request.POST.get("user_name")
        password = request.POST.get("pwd")
        email = request.POST.get("email")
        allow = request.POST.get("allow")
        if not all([username,password,email]):
            return render(request, 'goods/register.html', {"merror": "请把数据填写完整"})
        if allow !='on':
            return render(request, 'goods/register.html', {"merror": "请勾选同意条款"})
        try:
            user =User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'goods/register.html', {'merror': '用户名已存在'})
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()
        return redirect(reverse('goods:index'))


def index(request):
    return render(request,'goods/index.html')

def list(request):
    return render(request,'goods/list.html')

def detail(request):
    return render(request,'goods/detail.html')