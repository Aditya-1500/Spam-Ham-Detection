import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

class MLModel():
    def __init__(self,tweets):
        self.tweets = tweets
        self.pipeline = Pipeline([
        ('bow', CountVectorizer(analyzer=self.text_process)),  # strings to token integer counts
        ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
        ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
        ])
    
        
    def text_process(self,mess):
        """
        Takes in a string of text, then performs the following:
        1. Remove all punctuation
        2. Remove all stopwords
        3. Returns a list of the cleaned text
        """
        # Check characters to see if they are in punctuation
        nopunc = [char for char in mess if char not in string.punctuation]
    
        # Join the characters again to form the string.
        nopunc = ''.join(nopunc)
        
        # Next just remove any stopwords
        return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

    def train_model(self):
        self.pipeline.fit(self.tweets['message'],self.tweets['label'])
    
    def predict(self,tweet):
        prediction = self.pipeline.predict([tweet])
        return prediction

tweets = pd.read_csv('media/HamSpamTweets.csv')
pipeline = MLModel(tweets)
pipeline.train_model()
# messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t',names=["label", "message"])


# msg_train, msg_test, label_train, label_test = \
# train_test_split(messages['message'], messages['label'], test_size=0.2)

# tweets = pd.read_csv('HamSpamTweets.csv')
# clf = MLModel(tweets)
# clf.train_model()
# print(clf.predict(msg_test.iloc[0])," - ",label_test.iloc[0])
# print(clf.predict(msg_test.iloc[1])," - ",label_test.iloc[1])
# print(clf.predict(msg_test.iloc[2])," - ",label_test.iloc[2])

