from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView
)
from django.urls import reverse_lazy
from .models import Label
from .forms import LabelForm
from task_manager.mixins import DeleteProtectionMixin
# Create your views here.


class LabelsListView(CustomListView):
    template_name = 'labels/index.html'
    model = Label
    context_object_name = 'labels'


class LabelCreateView(CustomCreateView):
    template_name = 'registration/form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = 'Label was created'
    extra_context = {'header': 'Create Label', 'button_text': 'create label'}


class LabelUpdateView(CustomUpdateView):
    template_name = 'registration/form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = 'Labels was updated'
    extra_context = {'header': 'Update Label', 'button_text': 'update label'}


class LabelDeleteView(DeleteProtectionMixin, CustomDeleteView):
    template_name = 'delete_form.html'
    model = Label
    success_url = reverse_lazy('labels')
    protected_url = reverse_lazy('labels')
    success_message = 'Label was deleted'
    protected_message = 'Impossible to delete because it is in use'
    extra_context = {'header': 'Delete Label', 'button_text': 'Yes, delete'}
