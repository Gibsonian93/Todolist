from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView

app_name="todo"

urlpatterns = [
    path('', TaskListView.as_view(), name = 'task_list'),
    path('create_task/', TaskCreateView.as_view(), name = 'task_create'),
    path('task_detail/<int:pk>/', TaskDetailView.as_view(), name= 'task_detail'),
    path('task_update/<int:pk>/', TaskUpdateView.as_view(), name = "task_update")
]
