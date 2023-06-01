from django.test import TestCase
from .forms import JobPostingForm, JobApplicationForm


class TestJobPostingForm(TestCase):
    """
    A suite of tests to check that the
    job posting form works as expected.
    """
    def test_required_fields(self):
        fields = [
            'title', 'salary', 'location', 'closing_date',
            'featured_image', 'company_overview', 'job_description',
            'requirements', 'benefits'
            ]
        for field in fields:
            form = JobPostingForm({field: ''})
            self.assertFalse(form.is_valid())


class TestJobApplicationForm(TestCase):
    """
    A suite of tests to check that the
    job application form works as expected.
    """

    def test_required_fields(self):
        fields = [
            'full_name', 'email', 'phone', 'linkedin', 'github_username',
            'why_company', 'why_role', 'why_you', 'supporting_docs',
        ]
        for field in fields:
            form = JobApplicationForm({field: ''})
            self.assertFalse(form.is_valid())
