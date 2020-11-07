from django.db import models

# Create your models here.
class SpamURLS(models.Model):
    spam_url = models.URLField(unique=True)

class HamSpamTweets(models.Model):
    tweet = models.TextField()
    label = models.CharField(max_length=15)

class Words_Users(models.Model):
    spammy_words = models.CharField(max_length=256)
    spammy_users = models.CharField(max_length=256)
