from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from platform_app.models import Project, Module
from django.forms import modelformset_factory
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, QuerySetPaginator
from platform_app.forms import ProjectForm, ModuleForm
from datetime import datetime
from django.utils.timezone import utc
# Create your views here.


@login_required
def view_module(request):
    username = request.session.get('user', '')
    Modulelist = Module.objects.all().order_by('-creationtime')
    return render(request,"module_manage.html",{"username":username,"modulelist":Modulelist, "type":"list"})


@login_required
def edit_module(request, id):
    # if this is a POST request we need to process the form data
    module_obj = Module.objects.get(id=id)
#    module_form = ModuleForm(instance=module_obj)
    print('module'+ str(module_obj))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print('module 2'+ str(module_obj.project))
        module_form = ModuleForm(request.POST, instance=module_obj)
        print('form'+ str(module_form))
        # check whether it's valid:
        if module_form.is_valid():
            print('form2'+ str(module_form))
            module = module_form.save(commit=False)
            module.creationtime = datetime.utcnow().replace(tzinfo=utc)
            print(module)
            module.save()
            module_form.save_m2m()
            return HttpResponseRedirect('/management/module_manage/')
        else:
            print(module_form.errors)
            return render(request, 'module_manage.html', {'module_obj': module_obj, "type":"edit"})
    else:
        if id:
            module_form = ModuleForm(instance=Module.objects.get(id=id))
        else:
            module_form = ModuleForm()
    return render(request, 'module_manage.html', {
        'module_obj': module_form,
        "id":id, 
        "type":"edit"
        })

@login_required
def add_module(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        module_form = ModuleForm(request.POST)
        # check whether it's valid:
        if module_form.is_valid():
            print(module_form)
            module = module_form.save(commit=False)
            module.creationtime = datetime.now()
            print(module)
            module.save()
            module_form.save_m2m()
            return HttpResponseRedirect('/management/module_manage/')
        else:
            print(module_form.errors)
            return render(request, 'module_manage.html', {'module_obj': module_form,"type":"add"})
    else:
        module_form = ModuleForm()
        print(module_form)

    return render(request, 'module_manage.html',{'module_obj':module_form, "type":"add"})

@login_required
def del_module(request,id):
    Module.objects.get(id=id).delete()
    return HttpResponseRedirect('/management/module_manage/')

