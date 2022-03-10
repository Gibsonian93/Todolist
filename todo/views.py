from asyncio import Task
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo.models import Task

class TaskListView(ListView):
    model = Task
    queryset = Task.objects.order_by('due_date')
    context_object_name = "task_list"

class TaskCreateView(CreateView):
    model = Task
    fields = ["title","due_date","description"]
    success_url = reverse_lazy('todo:task_list')
