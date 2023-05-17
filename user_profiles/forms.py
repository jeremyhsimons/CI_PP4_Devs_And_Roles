from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from .models import UserProfile


class AddUserProfileForm(forms.ModelForm):
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
        
    def __init__(self, *args, **kwargs):
        super(AddUserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
