from django.contrib import admin
from platform_app.models import Project, Module
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','status','creationtime']

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','project','creationtime']
admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
# Register your models here.
