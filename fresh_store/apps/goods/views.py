from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'goods/login.html')

def register(request):
    return render(request,'goods/register.html')

def index(request):
    return render(request,'goods/index.html')

def list(request):
    return render(request,'goods/list.html')

def detail(request):
    return render(request,'goods/detail.html')