from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect


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
            if user is not None:
                response = HttpResponseRedirect('/project_manage/')
                request.session['user'] = username
                return response
            else:
                return render(request, "index.html", {"error": "用户登录失败"})


def project_manage(request):
    username = request.session.get('user', '')
    return render(request, 'project_manage.html', {"user": username})


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response
