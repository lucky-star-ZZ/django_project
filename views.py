from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

from . import views


def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)

def runoob2(request):
    views_name = "菜鸟教程"
    return render(request, "runoob.html", {"name": views_name})

def runoob3(request):
    views_name = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "runoob.html", {"views_list": views_name})

#字典
def runoob4(request):
    views_dict = {"name": "菜鸟教程"}
    return render(request, "runoob.html", {"views_dict": views_dict})


####过滤器

#defalut
def runoob5(request):
    name = 0
    return render(request, "runoob.html", {"name": name})

#safe
def runoob6(request):
    views_str = "<a href = 'https://www.runoob.com/'>点击跳转</a>"
    return render(request, "runoob.html", {"views_str": views_str})