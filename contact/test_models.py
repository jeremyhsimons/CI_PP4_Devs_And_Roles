from django.test import TestCase
from .models import ContactMessage


class TestContactModel(TestCase):
    """
    A test for the string method
    of the ContactMessage model.
    """
    def test_string_method(self):
        message = ContactMessage.objects.create(
            pk=100,
            full_name='Sebastian Smith',
            email='seb@email.com',
            message='Your site is broken'
        )
        self.assertEqual(str(message), f'{100}-Sebastian Smith')
