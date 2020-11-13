from django.db import models
from django.contrib import auth
from django.urls import reverse_lazy

# Create your models here.
class UsersDB(models.Model):
    user = models.OneToOneField(auth.models.User,on_delete=models.CASCADE)
    spamurl_user = models.FileField(upload_to='classify/files',blank=True)
    hamspamtweets_user = models.FileField(upload_to='classify/files',blank=True)
    spammywordsusers_user = models.FileField(upload_to='classify/files',blank=True)

    def get_absolute_url(self):
        return reverse_lazy("classify_spam_ham")

    def __str__(self):
        return self.user.username
