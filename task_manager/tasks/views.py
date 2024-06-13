from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from task_manager.mixins import PermitModifyUserMixin

# Create your views here.
class ListTaskView(ListView):
    template_name = 'tasks/index.html'
    model = Task
    context_object_name = 'tasks'
    extra_context = {'button_text': 'Show'}

class CreateTaskView(CreateView):
    template_name = 'registration/form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = 'Task was created'
    extra_context = {'header': 'Create task', 'button_text': 'Create task'}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class UpdateTaskView(UpdateView):
    template_name = 'registration/form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = 'Task was updated'
    extra_context = {'header': 'Update task', 'button_text': 'Update task'}

class DeleteTaskView(PermitModifyUserMixin, DeleteView):
    template_name = 'delete_form.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = 'Task was deleted'
    extra_content = {'header': 'Delete task', 'button_text': 'Yes, delete'}

class DetailTaskView(DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task
