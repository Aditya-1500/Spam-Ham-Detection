from django.shortcuts import render
from django.http import HttpResponse
from .SMS_Ham_Spam import pipeline
from django.contrib import auth
import pandas as pd
from .forms import getFile,getMessage
from users.models import UsersDB

def handle_uploaded_file(file):
    predictions = []
    with file.open() as f:
        for line in f:
            prediction = pipeline.predict([line])
            predictions.append([line,prediction[0]])
    return predictions

# Create your views here.
def HomeView(request):
    return render(request,"home.html")

def classify_spam_ham(request):
    f_form = getFile()
    m_form = getMessage()
    return render(request,"classify/classify_spam_ham.html",{'f_form':f_form,'m_form':m_form})

def ResultView(request):

    if request.user.is_authenticated:
        user_id = auth.models.User.objects.filter(username=request.user)[0]
        file = UsersDB.objects.filter(user=user_id)[0].hamspamtweets_user
        data = pd.read_csv(file,sep='\t',names=["label", "message"])
        pipeline.fit(data['message'],data['label'])

    if request.method == 'POST':
        form = getFile(request.POST,request.FILES)
        if form.is_valid():
            if 'file' in request.FILES:
                inp_file = request.FILES['file']
                predictions = handle_uploaded_file(inp_file)
                return render(request,"classify/result.html",context={'predictions':predictions})
            else:
                message = request.POST['message']
                prediction = pipeline.predict([message])
                predictions = [message,prediction[0]]
            return render(request,"classify/result.html",context={'predictions':predictions})

    else:
        form = getFile()
        return render(request,"classify/result.html",context={'message':"Hello World",'prediction':"Checking"})
