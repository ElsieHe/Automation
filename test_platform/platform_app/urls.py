from django.urls import path, re_path
from . import views

app_name = "management"
urlpatterns = [
    path("", views.view_project),
    path("view_project/", views.view_project),
    path('edit_project/<int:id>/', views.edit_project),
    path("del_project/<int:id>", views.del_project),
    path("add_project/", views.add_project),
]