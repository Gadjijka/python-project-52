from django.views.generic import ListView
from task_manager.views import CustomCreateView, CustomUpdateView, CustomDeleteView
from task_manager.users.models import User
from .forms import RegisterUserForm, UpdateUserForm
from task_manager.mixins import CustomLoginMixin, PermitModifyUserMixin, DeleteProtectionMixin
from django.urls import reverse_lazy
# Create your views here.

class UsersListView(ListView):
    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UserCreateView(CustomCreateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_message = 'User is successfully registered'
    extra_context = {'header':'Registration', 'button_text': 'Sign up'}


class UserUpdateView(CustomLoginMixin, PermitModifyUserMixin, CustomUpdateView):
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('users')
    success_message = 'User is successfully updated'
    extra_context = {'header': 'Update user', 'button_text': 'Update'}


class UserDeleteView(CustomLoginMixin, PermitModifyUserMixin, DeleteProtectionMixin, CustomDeleteView):
    model = User
    success_url = reverse_lazy('users')
    success_message = 'User successfully deleted'
    protected_message = 'Cannot delete a user because it is in use'
    protected_url = reverse_lazy('users')
    extra_context = {'header': 'Delete user', 'button_text': 'Yes, delete'}
