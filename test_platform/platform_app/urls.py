from django.urls import path, re_path
from platform_app.views import project_views
from platform_app.views import module_views

app_name = "management"
urlpatterns = [
    path("", project_views.view_project),
    path("project_manage/", project_views.view_project),
    path('edit_project/<int:id>/', project_views.edit_project),
    path("del_project/<int:id>", project_views.del_project),
    path("add_project/", project_views.add_project),
    path("module_manage/", module_views.view_module),
    path('edit_module/<int:id>/', module_views.edit_module),
    path("del_module/<int:id>", module_views.del_module),
    path("add_module/", module_views.add_module),

]