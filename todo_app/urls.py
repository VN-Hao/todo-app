from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_app, name="app-page"),
    path("api/add-task/", views.add_task, name="add-task"),
    path("api/remove-task/", views.remove_task, name="remove-task"),
    path("api/update-status/", views.update_status, name="update-status")
]