from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField()