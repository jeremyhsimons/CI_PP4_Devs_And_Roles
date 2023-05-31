from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    A test suite to check the contact form 
    functions correctly.
    """
    def test_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())

    def test_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
