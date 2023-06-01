from django.test import TestCase
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import ContactMessage
from .forms import ContactForm
from .views import CreateContactMessage


class TestCreateContactMessage(TestCase):
    """
    A test to check that the CreateContactMessage view
    works as expected.
    """
    def setUp(self):
        # set up user for the test
        self.user = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user.save()
        self.user.set_password('hellotestuser101')
        self.user.save()

    def tearDown(self):
        self.user.delete()
