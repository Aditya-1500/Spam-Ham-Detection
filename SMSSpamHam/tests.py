from django.test import TestCase
from Classifiers.QuotientFilter import QuotientFilter
from Classifiers.LSH import LSH
from Classifiers.Classifier4 import pipeline
import pandas as pd

class ClassifierTest(TestCase):
    
    def test_pipeline_prediction(self):
        tweet_ham = "Sorry, I'll call later in meeting."
        tweet_spam = "As a valued customer, I am pleased to advise you that following recent review of your Mob No. you are awarded with a Â£1500 Bonus Prize, call 09066364589"
        self.assertEqual(pipeline.predict(tweet_ham)[0].capitalize(),"Ham")
        self.assertEqual(pipeline.predict(tweet_spam)[0].capitalize(),"Spam")

    def test_quotient_filter(self):
        self.spam_urls = pd.read_csv('media/SpamUrls.csv')
        self.spammy_words_users = pd.read_csv('media/SpammyWordsUsers.csv')
        self.qf_urls = QuotientFilter()
        self.qf_words = QuotientFilter()
        self.qf_users = QuotientFilter()

        for u in self.spam_urls['url']:
            self.qf_urls.addKey(u)

        self.spam_words = list(self.spammy_words_users['spam_words'])
        self.spam_users = list(self.spammy_words_users['spam_users'])

        for w in self.spam_words:
            self.qf_words.addKey(w)
        for u in self.spam_users:
            self.qf_users.addKey(u)

        spammy_word = "Free"
        spammy_user = "Dawn Deleon"
        spammy_url = "http://webb.com/"
        ham_word = "Regular"
        ham_user = "Bill Gates"
        ham_url = "https://www.google.com"

        self.assertEqual(self.qf_urls.lookup(spammy_url),"Spam")
        self.assertEqual(self.qf_urls.lookup(ham_url),"Ham")
        self.assertEqual(self.qf_users.lookup(spammy_user),"Spam")
        self.assertEqual(self.qf_users.lookup(ham_user),"Ham")
        self.assertEqual(self.qf_words.lookup(spammy_word),"Spam")
        self.assertEqual(self.qf_words.lookup(ham_word),"Ham")

    def test_lsh(self):
        self.hsClusters = pd.read_csv('media/Ham_Spam_Clusters.csv')
        self.lsh = LSH()
        
        hamCl = list(self.hsClusters['Ham'])
        spamCl = list(self.hsClusters['Spam'])
        self.lsh.update(hamCl,spamCl)

        tweet_ham = "Sorry, I'll call later in meeting."
        tweet_spam = "As a valued customer, I am pleased to advise you that following recent review of your Mob No. you are awarded with a Â£1500 Bonus Prize, call 09066364589"
        
        self.assertEqual(self.lsh.query(tweet_ham),"Ham")
        self.assertEqual(self.lsh.query(tweet_spam),"Spam")
        
