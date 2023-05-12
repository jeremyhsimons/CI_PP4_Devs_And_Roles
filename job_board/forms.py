from .models import JobPosting
from django import forms


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ('title', 'salary', 'location', 'closing_date',
                  'featured_image', 'company_overview', 'job_description',
                  'requirements', 'benefits')
