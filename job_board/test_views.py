from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal imports
from .views import (
    JobPostingList, 
    JobPostingDetail, 
    CreateJobPosting,
    UpdateJobPosting, 
    delete_job_posting
)
from .models import JobApplication, JobPosting


class TestJobPostingList(TestCase):
    """
    A class to check that the user gets the list of postings
    when they are at the home page '/'.
    """
    def test_get_jobs(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestJobPostingDetail(TestCase):
    """
    A class to test that the site can get
    the correct job posting details.
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.view = JobPostingDetail.as_view()
        self.user = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user.save()

        self.job = JobPosting.objects.create(
            title='test job posting 101',
            posted_by=self.user,
            salary=123456,
            location='London',
            closing_date="2025-05-05",
            company_overview="this is a test company",
            job_description="this is a test JD",
            requirements="These are test requirements",
            benefits="These are test benefits",
            approved=True,
            id='101'
        )
        self.job.save()

    def test_get_job_posting_details(self):
        # test that url path for test job post works
        request = self.factory.get(f'{self.job.pk}/')
        response = self.view(request, self.job.pk)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.user.delete()
        self.job.delete()


class TestCreateJobPosting(TestCase):
    """
    A class to check that the user can access the
    job posting form and submit it successfully.
    """
    def setUp(self):
        self.user = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user.save()

    def test_get_job_post_form(self):
        # check the user can access the form when logged in.
        self.client.force_login(user=self.user)
        response = self.client.get('/create-job-post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'create-job-post.html'
        )

    def test_job_post_form_submit(self):
        # check whether user can submit the form.
        self.client.force_login(user=self.user)
        response = self.client.post(
            '/create-job-post/',
            {
                'title': 'test title',
                'salary': 20000,
                'location': 'Londion',
                'closing_date': '2025-05-05',
                'company_overview': 'Company',
                'job_description': 'job',
                'requirements': 'requirements',
                'benefits': 'nice stuff',
                'id': 102
            })
        print(response)
        self.assertEqual(response.status_code, 200)
        # check it exists in db
        unapproved_jobs = JobPosting.objects.filter(approved=False)
        self.assertEquals(unapproved_jobs[0].title, 'test title')

    def test_invalid_jobpost_submission(self):
        # check that user cannot submit invalid form.
        self.client.force_login(user=self.user)
        response = self.client.post(
            '/create-job-post/',
            {
                'title': '',
                'salary': 20000,
                'location': '',
                'closing_date': '',
                'company_overview': '',
                'job_description': '',
                'requirements': '',
                'benefits': '',
                'id': 102
            })
        self.assertFalse(
            JobPosting.objects.filter(id=102).exists()
        )

    def tearDown(self):
        self.user.delete()


class TestUpdateJobPosting(TestCase):
    """
    Tests whether the user can access their job posting
    and update the details with the form provided.
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.view = UpdateJobPosting.as_view()
        self.user = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user.save()

        self.job = JobPosting.objects.create(
            title='test job posting 101',
            posted_by=self.user,
            salary=123456,
            location='London',
            closing_date="2025-05-05",
            company_overview="this is a test company",
            job_description="this is a test JD",
            requirements="These are test requirements",
            benefits="These are test benefits",
            approved=True,
            id='103'
        )
        self.job.save()

    def test_get_update_job(self):
        self.client.force_login(self.user)
        response = self.client.get('/update-job-post/103')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update-job-post.html')

    def test_submit_updated_job(self):
        self.client.force_login(self.user)
        response = self.client.post(
            f'/update-job-post/{self.job.id}',
            {
                'title': 'updated',
                'salary': 654321,
                'location': 'updated0',
                'closing_date': '2026-05-05',
                'company_overview': 'updated1',
                'job_description': 'updated2',
                'requirements': 'updated3',
                'benefits': 'updated4',
            }
            )
        self.assertEquals(response.status_code, 302)
        self.assertTrue(
            JobPosting.objects.filter(title='updated').exists()
            )

    def test_submit_invalid_updated_job(self):
        self.client.force_login(self.user)
        response = self.client.post(
            f'/update-job-post/{self.job.id}',
            {
                'title': '',
                'salary': 654321,
                'location': '',
                'closing_date': '',
                'company_overview': '',
                'job_description': '',
                'requirements': '',
                'benefits': '',
            }
        )
        self.assertEquals(response.status_code, 200)
        self.assertFalse(
            JobPosting.objects.filter(title='').exists()
        )

    def tearDown(self):
        self.user.delete()
        self.job.delete()