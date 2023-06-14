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
            'linkedin': 'Provide a url to your LinkedIn page',
            'github_username': 'Provide your GitHub username',
            'job_seeker': 'Tick the box if you are seeking work',
            'recruiter': 'Tick the box if you are hiring',
            'location': 'Where are you currently based?',
            'years_experience': 'Years experience. If none, put 0.',
            'education': 'Provide details of your education history',
            'work_experience': 'Provide details of your work history',
            'interests': 'Provide details of your interests outside of work',
            'roles_open_to': 'Give examples of roles you are pursuing',
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
