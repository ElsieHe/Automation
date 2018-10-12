from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from django.utils.timezone import utc
# Create your views here.


def index(request):
    return render(request, "index.html")


def login_action(request):
    """

    :type request: object
    """
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或者密码为空"})
        else:
            user = auth.authenticate(username=username, password=password)
            print(user)
            print(password)
            if user is not None:
                auth.login(request,user)
                request.session['user'] = username
                response = HttpResponseRedirect('/management/')

                return response
            else:
                return render(request, "index.html", {"error": "用户登录失败"})


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response
