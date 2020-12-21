from django.db import models
from django.contrib import auth
from django.urls import reverse_lazy
from django.forms import ValidationError

def validate_file_extension(value):
         if not value.name.endswith('.csv'):
             raise ValidationError("Only CSV file is accepted")

# Create your models here.
class UsersDB(models.Model):
    user = models.OneToOneField(auth.models.User,on_delete=models.CASCADE)
    spamurl_user = models.FileField(upload_to='classify/files',blank=True,validators=[validate_file_extension])
    hamspamtweets_user = models.FileField(upload_to='classify/files',blank=True,validators=[validate_file_extension])
    spammywordsusers_user = models.FileField(upload_to='classify/files',blank=True,validators=[validate_file_extension])

    def get_absolute_url(self):
        return reverse_lazy("classify_spam_ham")

    def __str__(self):
        return self.user.username
