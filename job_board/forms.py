from django import forms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import JobPosting, JobApplication


class JobPostingForm(forms.ModelForm):
    """
    A class to package form fields for  the 'create job posting' page.
    """
    class Meta:
        model = JobPosting
        fields = ('title', 'salary', 'location', 'closing_date',
                  'featured_image', 'company_overview', 'job_description',
                  'requirements', 'benefits')
        labels = {
            'title': 'Job Title / Position',
            'salary': 'Expected Salary',
            'location': 'Location',
            'closing_date': 'Closing date YYYY-MM-DD',
            'featured_image': 'Choose an image or company logo to display.',
            'company_overview': 'Company Overview',
            'job_description': 'Job Description',
            'requirements': 'Requirements',
            'benefits': 'Benefits',
        }


class JobApplicationForm(forms.ModelForm):
    """
    A class to package form fields for  the 'create job application' page.
    """
    class Meta:
        model = JobApplication
        fields = ('full_name', 'email', 'phone', 'linkedin', 'github_username',
                  'why_company', 'why_role', 'why_you')
        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone number',
            'linkedIn': 'A url to your LinkedIn account is required',
            'github_username': 'Your GitHub username is required',
            'why_company': 'Explain your interest in the company. (2000 chars)',
            'why_role': 'Explain your interest in the role. (2000 chars)',
            'why_you': 'Explain your suitability. (2000 chars)',
        }
