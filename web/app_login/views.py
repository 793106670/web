from django.shortcuts import render
#! -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from web.app_login.login_pkg.users import UserCls

def hello(request,):
    return HttpResponse("hello")

# request是包含当前web请求信息的对象，是类django.http.HttpRequest的一个实例
def pagelogin(request):

    return render_to_response('login.html', {'welcome_message': 'welcome to our page'})

def display_user(request):
    show_dict = {"title": "user list", "user_ls": []}
    usr_obj = UserCls()
    user_ls = usr_obj.get_all()
    show_dict["user_ls"] = user_ls
    return render_to_response('show_user.html', show_dict)