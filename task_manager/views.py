from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class UserLogin(LoginView):
    template_name = 'form.html'
    next_page = reverse_lazy('home')

class UserLogout(View):
    pass
