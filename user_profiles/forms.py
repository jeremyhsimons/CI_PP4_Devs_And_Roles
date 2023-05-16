from django import forms
from .models import UserProfile


class AddUserProfileForm(forms.ModelForm):
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
            'roles_open_to',
        )
