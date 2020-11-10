from django.shortcuts import render
from django.contrib.auth import login,logout
from django.views.generic import CreateView
from .forms import UserCreateForm
from django.urls import reverse_lazy
# Create your views here.
class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
