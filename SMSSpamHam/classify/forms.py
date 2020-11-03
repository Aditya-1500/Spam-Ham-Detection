from django import forms

class getFile(forms.Form):
    file = forms.FileField(required=False)

class getMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea,required=False)
