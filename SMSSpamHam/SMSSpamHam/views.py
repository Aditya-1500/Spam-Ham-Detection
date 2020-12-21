from django.views.generic import TemplateView
from django.shortcuts import render

def HomeView(request):
    return render(request,"home.html")

class ThanksPage(TemplateView):
    template_name = "thanks.html"
