from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import UserProfile, Message


class AddUserProfileForm(forms.ModelForm):
    """
    A class to package form data for add user profile page.
    """
    job_seeker = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = (
            'first_name',
            'last_name',
            'linkedin',
            'github_username',
            'job_seeker',
            'recruiter',
            'location',
            'years_experience',
            'education',
            'work_experience',
            'interests',
            'roles_open_to',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'linkedin': 'LinkedIn URL',
            'github_username': 'GitHub username',
            'job_seeker': 'Tick the box if you are seeking work',
            'recruiter': 'Tick the box if you are hiring',
            'location': "Where you're based?",
            'years_experience': 'Years of experience',
            'education': 'Education History',
            'work_experience': 'Work History',
            'interests': 'Interests',
            'roles_open_to': 'Your Ideal Roles',
        }

    def __init__(self, *args, **kwargs):
        super(AddUserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()


class MessageUser(forms.ModelForm):
    """
    A class to package form data for add user profile page.
    """
    class Meta:
        model = Message
        fields = ('first_name', 'last_name', 'email', 'message')
