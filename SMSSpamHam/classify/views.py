from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
import pandas as pd
import re
from .forms import getFile,getMessage
from users.models import UsersDB

from Classifiers.QuotientFilter import QuotientFilter
from Classifiers.LSH import LSH
from Classifiers.Classifier4 import pipeline

def handle_uploaded_file(file):
    predictions = []
    with file.open() as f:
        for line in f:
            prediction = pipeline.predict([line.decode('utf-8')])
            predictions.append([line.decode('utf-8'),prediction[0]])
    return predictions

def predictSH(tweet,qf_urls,lsh,qf_users,qf_words):
    # user,url,message = tweet[0],tweet[1],tweet[2]
    user = tweet[0]
    message = tweet[1]
    urls_message = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',message)
    # user = user.split(':')[1]
    predictions = []
    p1 = "Ham"
    for url in urls_message:
        if qf_urls.lookup(url) == "Spam":
            p1 = "Spam"
    p2 = lsh.query(message)
    p3 = qf_users.lookup(user)
    hamW = 0
    spamW = 0
    for word in message.split(" "):
        if qf_words.lookup(word) == "Ham":
            hamW += 1
        else:
            spamW += 1
    if hamW > spamW:
        p4 = "Ham"
    else:
        p4 = "Spam"

    p5 = pipeline.predict(message)[0]

    predictions.append(p1)
    predictions.append(p2)
    predictions.append(p3)
    predictions.append(p4)
    predictions.append(p5)

    hp,sp = 0,0
    for p in predictions:
        if p == 'Ham':
            hp += 1
        else:
            sp += 1

    if hp > sp:
        prediction = "Ham"
    else:
        prediction = "Spam"
    return prediction

# Create your views here.

def classify_spam_ham(request):
    f_form = getFile()
    m_form = getMessage()
    return render(request,"classify/classify_spam_ham.html",{'f_form':f_form,'m_form':m_form})

def ResultView(request):

    spam_urls = pd.read_csv('media/SpamUrls.csv')
    hsClusters = pd.read_csv('media/Ham_Spam_Clusters.csv')
    spammy_words_users = pd.read_csv('media/SpammyWordsUsers.csv')
    qf_urls = QuotientFilter()
    lsh = LSH()
    qf_words = QuotientFilter()
    qf_users = QuotientFilter()

    if request.user.is_authenticated:
        user_id = auth.models.User.objects.filter(username=request.user)[0]
        if UsersDB.objects.filter(user=user_id)[0].spamurl_user:
            spamurls_file = UsersDB.objects.filter(user=user_id)[0].spamurl_user
            spam_urls = pd.read_csv(spamurls_file)
        if UsersDB.objects.filter(user=user_id)[0].hamspamtweets_user:
            hstweets_file = UsersDB.objects.filter(user=user_id)[0].hamspamtweets_user
            hsClusters = pd.read_csv(hstweets_file)
        if UsersDB.objects.filter(user=user_id)[0].spammywordsusers_user:
            spammy_wu_file = UsersDB.objects.filter(user=user_id)[0].spammywordsusers_user
            spammy_words_users = pd.read_csv(spammy_wu_file)

    for u in spam_urls['url'][:1000]:
        qf_urls.addKey(u)

    hamCl = list(hsClusters['Ham'])
    spamCl = list(hsClusters['Spam'])
    lsh.update(hamCl,spamCl)

    spam_words = list(spammy_words_users['spam_words'])
    spam_users = list(spammy_words_users['spam_users'])

    for w in spam_words[:1000]:
        qf_words.addKey(w)
    for u in spam_users[:1000]:
        qf_users.addKey(u)

    form = getFile()
    m_form = getMessage();
    if request.method == 'POST':
        form = getFile(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            if 'file' in request.FILES:
                inp_file = request.FILES['file']
                predictions = []
                tweets_file = pd.read_csv(inp_file)
                for i in range(len(tweets_file)):
                        tweet = [tweets_file.iloc[i]['Username'],tweets_file.iloc[i]['Tweet']]
                        # print(tweet)
                        prediction = predictSH(tweet,qf_urls,lsh,qf_users,qf_words)
                        predictions.append(['\n'.join(tweet),prediction])
                return render(request,"classify/result.html",context={'predictions':predictions})
            else:
                tweet = request.POST['message'].split('\n')
                predictions = []
                prediction = predictSH(tweet,qf_urls,lsh,qf_users,qf_words)
                predictions.append(['\n'.join(tweet),prediction])
                print(tweet)
            return render(request,"classify/result.html",context={'predictions':predictions})
        # else:
        #     print("Here")
        #     form = getFile()
        #     m_form = getMessage()
        #     print(form.errors)
    return render(request,"classify/classify_spam_ham.html",{'f_form':form,'m_form':m_form})