from django.test import TestCase, RequestFactory
from django.contrib.messages.middleware import MessageMiddleware
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

    def test_get_contact_page(self):
        # checks that the correct page and template is retrieved from db.
        response = self.client.get('/contact/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_sending_message(self):
        # checks that sending a message results in redirect to home page.
        self.client.force_login(self.user)
        response = self.client.post(
            '/contact/contact/',
            {
                'full_name': self.user.username,
                'email': self.user.email,
                'message': 'This is a new message'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_sending_invalid_message(self):
        """
        Checks that sending an empty message
        returns an error.
        """
        self.client.force_login(self.user)
        response = self.client.post(
            '/contact/contact/',
            {
                'full_name': self.user.username,
                'email': self.user.email,
                'message': ''
            }
        )
        self.assertRedirects(response, '/contact/contact/')

    def tearDown(self):
        self.user.delete()
