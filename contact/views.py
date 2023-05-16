from django.shortcuts import render, redirect
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

    def post(self, request, *args, **kwargs):
        """
        Submits completed forms to the database
        after checking if the user is signed in 
        and grabbing user details.
        """
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            if request.user:
                form.instance.user = request.user
            form.save()
            return redirect('home')
        else:
            form = ContactForm()
            return redirect('contact')
