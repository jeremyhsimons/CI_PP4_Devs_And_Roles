from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Message


class TestUserProfile(TestCase):
    """
    Checks that UserProfile methods work as expected.
    """
    def setUp(self):
        self.user = User.objects.create(
            username='Palin',
            password='hellopalin123',
            email='mpalin@email.com',
            id=2102
        )
        self.user.save()

        self.profile = UserProfile.objects.update(
            first_name="Michael",
            last_name="Palin",
            linkedin="michaelpalin/linkedin.com",
            github_username="mpalin",
            job_seeker=True,
            recruiter=False,
            location="Yorkshire",
            years_experience=25
        )

    def test_profile_created(self):
        profile = UserProfile.objects.filter().last()
        self.assertEquals(profile.user.username, 'Palin')
        self.assertEquals(profile.first_name, 'Michael')

    def test_user_profile_str(self):
        profile = UserProfile.objects.filter().last()
        self.assertTrue(str(profile), 'Palin')

    def tearDown(self):
        self.user.delete()


class TestMessage(TestCase):
    """
    Checks that the Message methods work as expected.
    """
    def setUp(self):
        self.user = User.objects.create(
            username='Cleese',
            password='hellocleese123',
            email='jcleese@email.com',
            id=2103
        )
        self.user.save()
        self.profile = UserProfile.objects.update(
            first_name="John",
            last_name="Cleese",
            linkedin="johncleese/linkedin.com",
            github_username="jcleese",
            job_seeker=True,
            recruiter=False,
            location="London",
            years_experience=30
        )

    def test_string_method(self):
        message = Message.objects.create(
            recipient=UserProfile.objects.get(user=self.user),
            first_name="Terry",
            last_name="Jones",
            message="Let's make a sketch show together.",
            email="tjones@montypython.com"
        )
        self.assertEqual(str(message), "Terry's message to John")

    def tearDown(self):
        self.user.delete()
