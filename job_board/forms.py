from .models import JobPosting, JobApplication
from django import forms


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ('title', 'salary', 'location', 'closing_date',
                  'featured_image', 'company_overview', 'job_description',
                  'requirements', 'benefits')

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('full_name', 'email', 'phone', 'linkedin', 'github_username'
                  'why_company', 'why_role', 'why_you')
