from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from platform_app.models import Project
from django.forms import modelformset_factory
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, QuerySetPaginator
from platform_app.forms import ProjectForm
from datetime import datetime
from django.utils.timezone import utc
# Create your views here.


@login_required
def view_project(request):
    username = request.session.get('user', '')
    Projectlist = Project.objects.all().order_by('-creationtime')
    return render(request,"project_manage.html",{"username":username,"projectlist":Projectlist, "type":"list"})


@login_required
def edit_project(request, id):
    # if this is a POST request we need to process the form data
    project_obj = Project.objects.get(id=id)
    project_form = ProjectForm(instance=project_obj)
    #print(project_obj)
    #print(project_form)
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
            return HttpResponseRedirect('/management/')
        else:
            print(project_form.errors)
            return render(request, 'project_manage.html', {'project_obj': project_obj, "type":"edit"})

    return render(request, 'project_manage.html', {'project_obj': project_form,"id":id, "type":"edit"})

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
            return HttpResponseRedirect('/management/')
        else:
            print(project_form.errors)
            return render(request, 'project_manage.html', {'project_obj': project_form,"type":"add"})
    else:
        project_form = ProjectForm()

    return render(request, 'project_manage.html',{'project_obj':project_form, "type":"add"})

@login_required
def del_project(request,id):
    Project.objects.get(id=id).delete()
    return HttpResponseRedirect('/management/')

