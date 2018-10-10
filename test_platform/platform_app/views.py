from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import Project
from django.forms import modelformset_factory
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, QuerySetPaginator
from .forms import ProjectForm
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
                response = HttpResponseRedirect('/view_project/')

                return response
            else:
                return render(request, "index.html", {"error": "用户登录失败"})



@login_required
def view_project(request):
    # Projectlist = Project.objects.all().order_by('-creationtime')
    # paginator = Paginator(Projectlist, 15, 2)
    # page = request.GET.get('page')
    # try:
    #     contacts =  paginator.page(page)
    # except PageNotAnInteger:
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     contacts = paginator.page(paginator.num_pages)
    # return render(request, "project_manage.html", {"projectlist":contacts})
    Projectlist = Project.objects.all().order_by('-creationtime')
    return render(request,"project_manage.html",{"projectlist":Projectlist})


@login_required
def edit_project(request, id):
    # if this is a POST request we need to process the form data
    project_obj = Project.objects.filter(id=id).first()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        project_form = ProjectForm(request.POST, instance=project_obj)
        # check whether it's valid:
        if project_form.is_valid():
            print(project_form)
            project = project_form.save(commit=False)
            project.creationtime = datetime.utcnow().replace(tzinfo=utc)
            print(project)
            project.save()
            project_form.save_m2m()
            return HttpResponseRedirect('/view_project/')
        else:
            print(project_form.errors)
            return render(request, 'edit_project.html', {'project_obj': project_obj})

    return render(request, 'edit_project.html', {'project_obj': project_obj})

@login_required
def add_project(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        project_form = ProjectForm(request.POST)
        # check whether it's valid:
        if project_form.is_valid():
            print(project_form)
            project = project_form.save(commit=False)
            project.creationtime = datetime.now()
            print(project)
            project.save()
            project_form.save_m2m()
            return HttpResponseRedirect('/view_project/')
        else:
            print(project_form.errors)
            return render(request, 'add_project.html', {'project_obj': project_form})

    return render(request, 'add_project.html')

@login_required
def del_project(request):
    id = request.GET.get("id")
    Project.objects.get(id=id).delete()
    return HttpResponseRedirect('/view_project/')

def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response
