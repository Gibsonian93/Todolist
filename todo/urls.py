from django.urls import path
from .views import TaskListView, TaskCreateView

app_name="todo"

urlpatterns = [
    path('', TaskListView.as_view(), name = 'task_list'),
    path('create_task/', TaskCreateView.as_view(), name = 'task_create')
]
