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
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('list_status')
    success_message = 'Status was created'
    extra_context = {'header': 'Create Status'}

class UpdateStatusView(UpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('list_status')
    success_message = 'Status was updated'
    extra_context = {'header': 'Update status'}

class DeleteStatusView(DeleteView):
    model = Status
    success_url = reverse_lazy('list_status')
    success_message = 'Status was deleted'
    extra_content = {'header': 'Delete status'}
