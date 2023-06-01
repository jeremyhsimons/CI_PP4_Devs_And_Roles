from django.test import TestCase
from .forms import AddUserProfileForm, MessageUser


class TestAddUserProfileForm(TestCase):
    """
    Checks that users cannot submit a user profile
    form with empty fields.
    """
    def test_required_fields(self):
        fields = [
            'first_name',
            'last_name',
            'linkedin',
            'github_username',
            'job_seeker',
            'recruiter',
            'location',
            'years_experience',
        ]
        for field in fields:
            form = AddUserProfileForm({field: ''})
            self.assertFalse(form.is_valid())


class TestMessageUser(TestCase):
    """
    Checks that users cannot send messages
    with empty fields.
    """
    def test_required_fields(self):
        fields = [
            'first_name', 'last_name', 'email', 'message'
        ]
        for field in fields:
            form = MessageUser({field: ''})
            self.assertFalse(form.is_valid())
