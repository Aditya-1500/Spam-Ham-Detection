from django.db import models
from django.contrib import auth

# Create your models here.
class UsersDB(models.Model):
    user = models.OneToOneField(auth.models.User,on_delete=models.CASCADE)
    spamurl_user = models.FileField(upload_to='classify/files')
    hamspamtweets_user = models.FileField(upload_to='classify/files')
    spammywordsusers_user = models.FileField(upload_to='classify/files')

    def __str__(self):
        return self.user.username
