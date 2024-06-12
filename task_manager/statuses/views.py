from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Status
from .forms import StatusForm
from django.urls import reverse_lazy

# Create your views here.
class ListStatusView(ListView):
    template_name = 'statuses/index.html'
    model = Status
    context_object_name = 'statuses'

class CreateStatusView(CreateView):
    template_name = 'registration/form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = 'Status was created'
    extra_context = {'header': 'Create Status', 'button_text': 'Create status'}

class UpdateStatusView(UpdateView):
    template_name = 'registration/form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = 'Status was updated'
    extra_context = {'header': 'Update status', 'button_text': 'Update status'}

class DeleteStatusView(DeleteView):
    template_name = 'delete_form.html'
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = 'Status was deleted'
    protected_message = ('Impossible to delete status because it is in use')
    extra_content = {'header': 'Delete status', 'button_text': 'Yes, delete'}
