from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'rating', 'text']
        labels = {'name': 'Full Name', 'text':'Your feedback'}