from django.views.generic import (TemplateView, CreateView, UpdateView, DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .mixins import ObjectContextMixin

class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template = 'form.html'
    next_page = reverse_lazy('home')
    success_message = 'You are logged in'
    extra_content = {'header': 'Log In', 'button_text': 'Login'}


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    success_message = 'You are log out'
    extra_content = {'header': 'Log out', 'button_text': 'Logout'}


class CustomCreateView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'


class CustomUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'

class CustomDeleteView(ObjectContextMixin, SuccessMessageMixin, DeleteView):
    template_name = 'delete_form.html'
