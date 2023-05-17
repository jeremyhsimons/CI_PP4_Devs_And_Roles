from django import forms
from .models import UserProfile


class AddUserProfileForm(forms.ModelForm):

    job_seeker = forms.BooleanField()
    recruiter = forms.BooleanField()

    class Meta:
        model = UserProfile
        fields = (
            'first_name',
            'last_name',
            'linkedin',
            'github_username',
            'location',
            'years_experience',
            'education',
            'work_experience',
            'interests',
            'roles_open_to',
        )


class AlternateProfileForm(forms.Form):
    
