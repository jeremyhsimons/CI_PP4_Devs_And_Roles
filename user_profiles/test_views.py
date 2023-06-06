from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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


class TestProfileDetail(TestCase):
    """
    Checks:
    1. Profile data successfully retrieved from db.
    2. Messages can be successfully sent to
    user associated with profile.
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.view = ProfileDetail.as_view()
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            pk='101'
        )
        self.user1.save()
        self.user2 = User.objects.create(
            username='testuser102',
            password='hellotestuser102',
            email='tester2@email.com',
            pk='102'
        )
        self.user2.save()

    def test_get_userprofile(self):
        self.client.force_login(user=self.user1)
        request = self.factory.get(
            'profile/profile_details/<int:pk>'
        )
        # User2's profile will have pk of 2 since it is the 2nd in db.
        response = self.view(request, '2')
        self.assertEqual(response.status_code, 200)

    def test_send_message(self):
        self.client.force_login(user=self.user1)
        response = self.client.post(
            '/profile/profile_details/2',
            {
                'first_name': 'Tester',
                'last_name': '101',
                'email': self.user1.email,
                'message': 'This is a test message',
            }
        )
        # user should get 200 http response with valid/invalid message.
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Message.objects.filter(first_name='Tester').exists()
        )

    def test_invalid_message(self):
        self.client.force_login(user=self.user1)
        self.client.post(
            '/profile/profile_details/2',
            {
                'first_name': '',
                'last_name': '',
                'email': '',
                'message': '',
            }
        )
        self.assertFalse(
            Message.objects.filter(first_name='').exists()
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()


class TestAddUserProfileDetails(TestCase):
    """
    Checks:
    1. The form to add details is retrieved from db
    2. User profile data submitted successfully
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            pk='101'
        )
        self.user1.save()

    def test_get_add_details_form(self):
        self.client.force_login(user=self.user1)
        response = self.client.get('/profile/add_user_profile_details/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_profile.html')

    def test_submit_valid_profile_details(self):
        self.client.force_login(user=self.user1)
        response = self.client.post(
            '/profile/add_user_profile_details/',
            {
                'first_name': 'Tester',
                'last_name': 'number1',
                'linkedin': 'randomurl',
                'github_username': 'randomusername',
                'job_seeker': True,
                'recruiter': False,
                'location': 'London',
                'years_experience': 5,
                'education': 'Diploma in full stack web development',
                'work_experience': 'Software tester',
                'interests': 'hunting wabbits',
                'roles_open_to': 'DevOps',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            UserProfile.objects.filter(interests='hunting wabbits').exists()
        )

    def test_submit_invalid_profile_details(self):
        self.client.force_login(user=self.user1)
        response = self.client.post(
            '/profile/add_user_profile_details/',
            {
                'first_name': '',
                'last_name': '',
                'linkedin': '',
                'github_username': '',
                'job_seeker': False,
                'recruiter': False,
                'location': '',
                'years_experience': '',
                'education': '',
                'work_experience': '',
                'interests': 'hunting wabbits',
                'roles_open_to': '',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            UserProfile.objects.filter(interests='hunting wabbits').exists()
        )

    def tearDown(self):
        self.user1.delete()


class TestEditUserProfileDetails(TestCase):
    """
    Checks:
    1. that the form is retrieved from the db.
    2. that valid submissions are saved to db.
    3. that invalid submissions are not saved to db.
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            pk='101'
        )
        self.user1.save()

    def test_get_edit_profile_form(self):
        self.client.force_login(user=self.user1)
        response = self.client.get('/profile/edit_profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')

    def test_submit_valid_edit_form(self):
        self.client.force_login(user=self.user1)
        response = self.client.post(
            '/profile/edit_profile/',
            {
                'first_name': 'Tester',
                'last_name': 'number1',
                'linkedin': 'randomurl',
                'github_username': 'randomusername',
                'job_seeker': True,
                'recruiter': False,
                'location': 'London',
                'years_experience': 5,
                'education': 'Diploma in full stack web development',
                'work_experience': 'Software tester',
                'interests': 'hunting wabbits',
                'roles_open_to': 'DevOps',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            UserProfile.objects.filter(interests='hunting wabbits').exists()
        )

    def test_submit_invalid_edit_form(self):
        self.client.force_login(user=self.user1)
        response = self.client.post(
            '/profile/edit_profile/',
            {
                'first_name': '',
                'last_name': '',
                'linkedin': '',
                'github_username': '',
                'job_seeker': False,
                'recruiter': False,
                'location': '',
                'years_experience': '',
                'education': '',
                'work_experience': '',
                'interests': 'hunting wabbits',
                'roles_open_to': '',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            UserProfile.objects.filter(interests='hunting wabbits').exists()
        )

    def tearDown(self):
        self.user1.delete()


class TestDeleteProfile(TestCase):
    """
    Checks:
    1. Delete page is successfully retrieved for user
    2. Profile can be successfully deleted on form submit.
    """

    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            pk='101'
        )
        self.user1.save()

    def test_get_delete_page(self):
        self.client.force_login(user=self.user1)
        response = self.client.get('/profile/delete_profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('delete_profile.html')

    def test_delete_profile(self):
        self.client.force_login(user=self.user1)
        response = self.client.post('/profile/delete_profile/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            UserProfile.objects.filter(user=self.user1).exists()
        )

    def tearDown(self):
        self.user1.delete()
