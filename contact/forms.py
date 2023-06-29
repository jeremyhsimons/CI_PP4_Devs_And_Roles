from django import forms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    A class for packaging form fields for the contact form.
    """
    class Meta:
        model = ContactMessage
        fields = ('full_name', 'email', 'message')
        labels = {
            'full_name': 'Write your name here',
            'email': 'Email address',
            'message': 'Details of your issue.'
        }
