from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import UsersDB

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"

class CustomDBForm(forms.ModelForm):

    class Meta:
        model = UsersDB
        fields = ('spamurl_user','hamspamtweets_user','spammywordsusers_user')
        widgets={
        'spamurl_user':forms.ClearableFileInput(attrs={'accept':'.csv'}),
        'hamspamtweets_user':forms.ClearableFileInput(attrs={'accept':'.csv'}),
        'spammywordsusers_user':forms.ClearableFileInput(attrs={'accept':'.csv'})
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['spamurl_user'].label = "Spam Urls "
        self.fields['hamspamtweets_user'].label = "Ham Spam Tweets "
        self.fields['spammywordsusers_user'].label = "Spammy Words and Users "
