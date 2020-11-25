# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:11:45 2020

@author: Aditya
"""

import pandas as pd
from faker import Faker

fakegen = Faker()

spam_urls = {'url':[]}
for i in range(10000):
    spam_urls['url'].append(fakegen.url())
    
messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t',names=["label", "message"])
hsClusters = {'Ham':[],'Spam':[]}

spam_words = []

for m in messages[messages['label']=='ham']['message']:
    hsClusters['Ham'].append(m)
    if len(hsClusters['Ham']) == 700:
        break

for m in messages[messages['label']=='spam']['message']:
    hsClusters['Spam'].append(m)
    for w in m.split(" "):
        if w not in spam_words and len(w) > 1:
            spam_words.append(w)
    if len(hsClusters['Spam']) == 700:
        break
            

spam_users = []
for i in range(len(spam_words)):
    spam_users.append(fakegen.name())

spammy_words_users = {'spam_words':spam_words,'spam_users':spam_users}

Spam_urls = pd.DataFrame(spam_urls)
HSClusters = pd.DataFrame(hsClusters)
SpammyWordsUsers = pd.DataFrame(spammy_words_users)

Spam_urls.to_csv('media/SpamUrls.csv',index=False)
HSClusters.to_csv('media/Ham_Spam_Clusters.csv',index=False)
SpammyWordsUsers.to_csv('media/SpammyWordsUsers.csv',index=False)

messages.to_csv('media/HamSpamTweets.csv')

    
