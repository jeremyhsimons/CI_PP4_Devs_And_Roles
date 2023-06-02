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

    def test_get_contact_page(self):
        # checks that the correct page and template is retrieved from db.
        response = self.client.get('/contact/contact/')
        print(self.user.username)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_sending_message(self):
        # checks that sending a message results in redirect to home page.
        response = self.client.post(
            '/contact/contact/',
            {
                'full_name': 'test user',
                'user': self.user,
                'email': 'franco@email.com',
                'message': 'Hello this is a message'
            }
            )
        self.assertRedirects(response, '/')

    def tearDown(self):
        self.user.delete()
