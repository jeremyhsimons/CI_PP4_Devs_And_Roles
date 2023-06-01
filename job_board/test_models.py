from django.test import TestCase
from django.contrib.auth.models import User
from .models import JobPosting, JobApplication


class TestJobPosting(TestCase):
    """
    Checks the str method works correctly.
    """
    def test_string_method(self):
        user1 = User.objects.create(username="Moab")
        job_posting = JobPosting.objects.create(
            title="software developer",
            salary=40000,
            closing_date='2025-05-05',
            posted_by=user1,
        )
        self.assertEqual(str(job_posting), "software developer")


class TestJobApplication(TestCase):
    """
    Checks the str method works correctly.
    """
    def test_string_method(self):
        user2 = User.objects.create(username="Canaan")
        user1 = User.objects.create(username="Moab")
        job_posting = JobPosting.objects.create(
            title="software developer",
            salary=40000,
            closing_date='2025-05-05',
            posted_by=user1,
        )
        application = JobApplication.objects.create(
            pk=2000,
            candidate=user2,
            job_posting=job_posting,
            full_name="John Smith",
            phone=123456789
        )
        self.assertEqual(str(application), "2000-John Smith")
