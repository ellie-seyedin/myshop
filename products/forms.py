from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(required=True, max_length=10, label="Full Name", help_text="Enter your name:", error_messages={"required": "You forgot to add your name", "max_length":"It's too long, make it shorter"})
    email = forms.EmailField(required=True)