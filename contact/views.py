from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm


class CreateContactMessage(generic.CreateView, SuccessMessageMixin):
    """
    A class for handling the contact page.
    """
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        """
        Submits completed forms to the database
        after checking if the user is signed in
        and grabbing user details.
        """
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(
                request, 'Your message has been sent to the site admin')
            return redirect('home')
        else:
            form = ContactForm()
            messages.error(
                request,
                'We could not process your message. Please try again.'
                )
            return redirect('contact')
