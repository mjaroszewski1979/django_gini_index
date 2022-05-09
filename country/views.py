from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from .forms import RegisterForm

class Login(LoginView):
    template_name = 'login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("This username is available")
