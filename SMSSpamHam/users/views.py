from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,get_user_model
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from .forms import UserCreateForm, CustomDBForm
from .models import UsersDB
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
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

            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        u = User.objects.filter(pk=self.request.user.pk)[0]
        u = UsersDB.objects.filter(user=u)[0]
        return url or reverse_lazy('profile',kwargs={'pk':u.pk})

def profile_redirect(request):
    u = UsersDB.objects.filter(user = request.user)[0]
    return HttpResponseRedirect(reverse('profile',kwargs={'pk':u.pk}))


class UserDetail(DetailView,LoginRequiredMixin):
    model = UsersDB

class UpdateCustomFiles(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'classify/classify_spam_ham.html'
    form_class = CustomDBForm
    model = UsersDB

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            u = self.model.objects.filter(user = self.request.user)[0]
            if request.POST['spamurl_user']:
                u.spamurl_user = request.POST['spamurl_user']
            if request.POST['hamspamtweets_user']:
                u.hamspamtweets_user = request.POST['hamspamtweets_user']
            if request.POST['spammywordsusers_user']:
                u.spammywordsusers_user = request.POST['spammywordsusers_user']
            clear_su = request.POST.get('spamurl_user-clear', False)
            clear_hst = request.POST.get('hamspamtweets_user-clear', False)
            clear_swu = request.POST.get('spammywordsusers_user-clear', False)
            if clear_su:
                # print('works')
                u.spamurl_user = ''
            if clear_hst:
                # print('works2')
                u.hamspamtweets_user = ''
            if clear_swu:
                # print('works3')
                u.spammywordsusers_user = ''
            u.save()
            print(u.spamurl_user,'-',request.POST['spamurl_user'])
            print(u.hamspamtweets_user)
            print(u.spammywordsusers_user)
            return HttpResponseRedirect(reverse_lazy('classify_spam_ham'))

        return render(request, self.template_name, {'form': form})
