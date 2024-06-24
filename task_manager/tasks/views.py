from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from .mixins import PermitDeleteTaskMixin
from django_filters.views import FilterView
from .filter import TaskFilter
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class ListTaskView(FilterView):
    template_name = 'tasks/index.html'
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    extra_context = {'button_text': 'Show'}


class CreateTaskView(SuccessMessageMixin, CustomCreateView):
    template_name = 'registration/form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = 'Task was created'
    extra_context = {'header': 'Create task',
                     'button_text': 'Create task'}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class UpdateTaskView(SuccessMessageMixin, CustomUpdateView):
    template_name = 'registration/form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = 'Task was updated'
    extra_context = {'header': 'Update task',
                     'button_text': 'Update task'}


class DeleteTaskView(PermitDeleteTaskMixin, SuccessMessageMixin, CustomDeleteView):
    template_name = 'delete_form.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = 'Task was deleted'
    extra_context = {'header': 'Delete task',
                     'button_text': 'Yes, delete'}


class DetailTaskView(DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task
