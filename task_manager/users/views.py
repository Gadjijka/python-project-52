from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView)
from .models import User
from .forms import RegisterUserForm, UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.mixins import PermitModifyUserMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _
# Create your views here.


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, _("You have successfully logged out."))
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/form.html'
    next_page = reverse_lazy('home')
    success_message = _('User is logged in')
    extra_context = {'header': _('Log In'), 'button_text': _('login')}


class UsersListView(ListView):
    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'registration/form.html'
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {'header': _('Registration'), 'button_text': _('Sign up')}


class UserUpdateView(PermitModifyUserMixin, SuccessMessageMixin, UpdateView):
    template_name = 'registration/form.html'
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    extra_context = {'header': _('Update user'), 'button_text': _('Update')}


class UserDeleteView(PermitModifyUserMixin, SuccessMessageMixin, DeleteView):
    template_name = 'delete_form.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
    protected_message = _('Cannot delete a user because it is in use')
    protected_url = reverse_lazy('users')
    extra_context = {'header': _('Delete user'), 'button_text': _('Yes, delete')}
