from django.test import TestCase
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal imports
from .views import (
    SeeAllProfiles,
    ProfileDetail,
    AddUserProfileDetails,
    ViewProfile,
    DeleteProfile
)
from .models import UserProfile, Message


class TestSeeAllProfules(TestCase):
    """
    Checks to see whether the SeeAllProfiles view returns the correct
    html document.
    """
    def test_get_all_profiles(self):
        response = self.client.get('/profile/see_all_profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'display_profiles.html')


class TestViewProfile(TestCase):
    """
    Checks to see whether the user can successfully access
    their profile details from the db.
    """
    def setUp(self):
        self.user = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user.save()

    def test_get_userprofile(self):
        self.client.force_login(user=self.user)
        response = self.client.get('/profile/view_profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_profile.html')

    def tearDown(self):
        self.user.delete()
