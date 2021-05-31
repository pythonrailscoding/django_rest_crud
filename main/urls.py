from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.api_overview_view, name="index"),
    path("task-list/", views.TaskList, name="list"),
    path("task-detail/<int:pk>/", views.TaskDetail, name="detail"),
    path("task-create/", views.TaskCreate, name="create"),
    path("task-update/<int:pk>/", views.TaskUpdate, name="update"),
    path("task-delete/<int:pk>/", views.TaskDelete, name="delete"),
]
