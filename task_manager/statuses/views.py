from task_manager.views import (
    CustomCreateView, CustomUpdateView, CustomDeleteView,
    CustomListView
)
from .models import Status
from .forms import StatusForm
from django.urls import reverse_lazy
from task_manager.mixins import DeleteProtectionMixin
# Create your views here.


class ListStatusView(CustomListView):
    template_name = 'statuses/index.html'
    model = Status
    context_object_name = 'statuses'


class CreateStatusView(CustomCreateView):
    template_name = 'registration/form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = 'Status was created'
    extra_context = {'header': 'Create Status', 'button_text': 'Create status'}


class UpdateStatusView(CustomUpdateView):
    template_name = 'registration/form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = 'Status was updated'
    extra_context = {'header': 'Update status', 'button_text': 'Update status'}


class DeleteStatusView(DeleteProtectionMixin, CustomDeleteView):
    template_name = 'delete_form.html'
    model = Status
    success_url = reverse_lazy('statuses')
    protected_url = reverse_lazy('statuses')
    success_message = 'Status was deleted'
    protected_message = ('Impossible to delete status because it is in use')
    extra_context = {'header': 'Delete status', 'button_text': 'Yes, delete'}
