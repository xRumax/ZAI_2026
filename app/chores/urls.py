from django.urls import path
from .views import *

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name = "task_list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name = "task_detail"),
    path("task/add/", TaskCreateView.as_view(), name = "task_create"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name = "task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name = "task_delete"),

    
    path("", ProjectListView.as_view(), name = "project_list"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name = "project_detail"),
    path("project/add/", ProjectCreateView.as_view(), name = "project_create"),
    path("project/<int:pk>/edit/", ProjectUpdateView.as_view(), name = "project_update"),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name = "project_delete"),
]


