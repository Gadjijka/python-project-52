from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView)
from .models import User
from .forms import RegisterUserForm, UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.mixins import PermitModifyUserMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/form.html'
    next_page = reverse_lazy('home')
    success_message = 'User is logged in'
    extra_context = {'header': 'Log In', 'button_text': 'Login'}


class UsersListView(ListView):
    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'registration/form.html'
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_message = 'User is successfully registered'
    extra_context = {'header': 'Registration', 'button_text': 'Sign up'}


class UserUpdateView(PermitModifyUserMixin, SuccessMessageMixin, UpdateView):
    template_name = 'registration/form.html'
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('users')
    success_message = 'User is successfully updated'
    extra_context = {'header': 'Update user', 'button_text': 'Update'}


class UserDeleteView(PermitModifyUserMixin, SuccessMessageMixin, DeleteView):
    template_name = 'delete_form.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = 'User successfully deleted'
    protected_message = 'Cannot delete a user because it is in use'
    protected_url = reverse_lazy('users')
    extra_context = {'header': 'Delete user', 'button_text': 'Yes, delete'}
