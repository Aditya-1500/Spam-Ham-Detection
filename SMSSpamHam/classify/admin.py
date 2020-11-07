from django.contrib import admin
from .models import SpamURLS, HamSpamTweets, Words_Users

# Register your models here.
admin.site.register(SpamURLS)
admin.site.register(HamSpamTweets)
admin.site.register(Words_Users)
