"""SMSSpamHam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from classify import views as c_views
from users import views as u_views
from .views import HomeView,ThanksPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name="home"),
    path('classify_spam_ham/',c_views.classify_spam_ham,name='classify_spam_ham'),
    path('result/',c_views.ResultView,name="result"),
    path('login/',u_views.Login.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('signup/',u_views.SignUp.as_view(),name="signup"),
    path('<int:pk>/update/',u_views.UpdateCustomFiles.as_view(),name="update"),
    path('<int:pk>/profile/',u_views.UserDetail.as_view(),name="profile"),
    path('redirect_profile/',u_views.profile_redirect,name="redirect_profile"),
    path('thanks/',ThanksPage.as_view(),name="thanks")
]
