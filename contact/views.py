from django.shortcuts import render
from django.views import generic, View
from .models import ContactMessage
from .forms import ContactForm


class CreateContactMessage(generic.CreateView):
    """
    A class for handling the contact page.
    """
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact.html'
