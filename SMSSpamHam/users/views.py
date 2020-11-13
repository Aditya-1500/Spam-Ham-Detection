from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,get_user_model
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from .forms import UserCreateForm, CustomDBForm
from .models import UsersDB
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            u = User.objects.filter(username=self.request.POST['username'])[0]
            new_user = UsersDB(user=u)
            new_user.save()

            return HttpResponse(self.request.POST['username'])

        return render(request, self.template_name, {'form': form})


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse_lazy('profile',kwargs={'pk':self.request.user.pk})

class UserDetail(DetailView,LoginRequiredMixin):
    model = UsersDB

class AddCustomFiles(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'classify/classify_spam_ham.html'
    form_class = CustomDBForm
    model = UsersDB

class UpdateCustomFiles(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'classify/classify_spam_ham.html'
    form_class = CustomDBForm
    model = UsersDB
