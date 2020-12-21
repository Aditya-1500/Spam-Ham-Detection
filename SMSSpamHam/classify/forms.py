from django import forms

def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV file is accepted")

class getFile(forms.Form):
    file = forms.FileField(required=False,validators=[validate_file_extension],
                            widget=forms.FileInput(attrs={'accept':'.csv'})
                            )

class getMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea(
                                    attrs={"placeholder":"Username\nTweet"}),
                                    required=False)
