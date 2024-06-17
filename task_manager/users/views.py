from task_manager.views import (CustomCreateView,
                                CustomUpdateView, CustomDeleteView)
from .models import User
from django.views.generic import ListView
from .forms import RegisterUserForm, UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.mixins import PermitModifyUserMixin
# Create your views here.


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class UserLoginView(LoginView):
    template_name = 'registration/form.html'
    next_page = reverse_lazy('home')
    success_message = 'User is logged in'
    extra_context = {'header': 'Log In', 'button_text': 'Login'}


class UsersListView(ListView):
    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UserCreateView(CustomCreateView):
    template_name = 'registration/form.html'
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_message = 'User is successfully registered'
    extra_context = {'header': 'Registration', 'button_text': 'Sign up'}


class UserUpdateView(PermitModifyUserMixin, CustomUpdateView):
    template_name = 'registration/form.html'
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('users')
    success_message = 'User is successfully updated'
    extra_context = {'header': 'Update user', 'button_text': 'Update'}


class UserDeleteView(PermitModifyUserMixin, CustomDeleteView):
    template_name = 'delete_form.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = 'User successfully deleted'
    protected_message = 'Cannot delete a user because it is in use'
    protected_url = reverse_lazy('users')
    extra_context = {'header': 'Delete user', 'button_text': 'Yes, delete'}
