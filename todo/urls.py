from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailView

app_name="todo"

urlpatterns = [
    path('', TaskListView.as_view(), name = 'task_list'),
    path('create_task/', TaskCreateView.as_view(), name = 'task_create'),
    path('task_detail/<int:pk>', TaskDetailView.as_view(), name= 'detail_task'),
]
