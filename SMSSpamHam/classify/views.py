from django.shortcuts import render
from django.http import HttpResponse
from .SMS_Ham_Spam import pipeline
import pandas as pd
from .forms import getFile,getMessage

# Create your views here.
def HomeView(request):
    f_form = getFile()
    m_form = getMessage()
    return render(request,"classify/home.html",{'f_form':f_form,'m_form':m_form})

def ResultView(request):

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

# def ResultView(request):
#     message = request.POST['message']
#     try:
#         file = request.FILES['file']
#     except :
#         print("File not found")
#     prediction = pipeline.predict([message])
#     return render(request,"classify/result.html",context={'message':message,'prediction':prediction[0]})


def handle_uploaded_file(file):
    predictions = []
    with file.open() as f:
        for line in f:
            prediction = pipeline.predict([line])
            predictions.append([line,prediction[0]])
    return predictions
