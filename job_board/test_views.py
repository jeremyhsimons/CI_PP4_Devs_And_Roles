from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal imports
from .views import (
    JobPostingList, 
    JobPostingDetail, 
    CreateJobPosting,
    UpdateJobPosting, 
    delete_job_posting,
    ViewApplicationDetails,
    CreateJobApplication,
    delete_application
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

class TestDeleteJobPosting(TestCase):
    """
    Checks whether:
    1. the delete view/url removes
    job posting from the db
    2. the posting cannot be deleted
    by another user
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user1.save()

        self.user2 = User.objects.create(
            username='testuser102',
            password='hellotestuser102',
            email='tester2@email.com',
            id='102'
        )
        self.user2.save()

        self.job = JobPosting.objects.create(
            title='test job posting 101',
            posted_by=self.user1,
            salary=123456,
            location='London',
            closing_date="2025-05-05",
            company_overview="this is a test company",
            job_description="this is a test JD",
            requirements="These are test requirements",
            benefits="These are test benefits",
            approved=True,
            id='104'
        )
        self.job.save()

    def test_delete_job_post(self):
        # checks that the user can remove the job post from the db
        self.client.force_login(user=self.user1)
        response = self.client.post(reverse(
            'delete-job-post', kwargs={'jobpost_id': '104'}
            ))
        self.assertRedirects(response, '/')
        self.assertFalse(
            JobPosting.objects.filter(id='104').exists()
            )

    def test_delete_other_users_job_post(self):
        # checks that the user can remove the job post from the db
        self.client.force_login(user=self.user2)
        response = self.client.post(reverse(
            'delete-job-post', kwargs={'jobpost_id': '104'}
            ))
        self.assertRedirects(response, '/')
        self.assertTrue(
            JobPosting.objects.filter(id='104').exists()
            )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.job.delete()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTING JOB APPLICATION VIEWS


class TestViewApplicationDetails(TestCase):
    """
    Checks that the user can successfully get
    the data for a job application from the db.
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user1.save()

        self.user2 = User.objects.create(
            username='testuser102',
            password='hellotestuser102',
            email='tester2@email.com',
            id='102'
        )
        self.user2.save()

        self.job = JobPosting.objects.create(
            title='test job posting 101',
            posted_by=self.user1,
            salary=123456,
            location='London',
            closing_date="2025-05-05",
            company_overview="this is a test company",
            job_description="this is a test JD",
            requirements="These are test requirements",
            benefits="These are test benefits",
            approved=True,
            id='104'
        )
        self.job.save()

        self.application = JobApplication.objects.create(
            candidate=self.user2,
            job_posting=self.job,
            full_name=self.user2.username,
            email=self.user2.email,
            phone=12345678,
            linkedin='url.com',
            github_username='github',
            why_company="I like it",
            why_role='I like it',
            why_you='I like myself',
            id='105'
        )
        self.application.save()

    def test_get_application_details(self):
        response = self.client.get('/application-detail/105')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application-detail.html")
        
    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.job.delete()
        self.application.delete()


class TestCreateJobApplication(TestCase):
    """
    Checks:
    1. That the application form is successfully retrieved from db
    2. That a valid submission is successfully saved to db
    3. That an invalid submission is not saved to db
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user1.save()

        self.user2 = User.objects.create(
            username='testuser102',
            password='hellotestuser102',
            email='tester2@email.com',
            id='102'
        )
        self.user2.save()

        self.job = JobPosting.objects.create(
            title='test job posting 101',
            posted_by=self.user1,
            salary=123456,
            location='London',
            closing_date="2025-05-05",
            company_overview="this is a test company",
            job_description="this is a test JD",
            requirements="These are test requirements",
            benefits="These are test benefits",
            approved=True,
            id='106'
        )
        self.job.save()

    def test_get_application_form(self):
        response = self.client.get('/apply/106')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'create-job-application.html'
        )

    def test_submit_valid_application(self):
        self.client.force_login(user=self.user2)
        response = self.client.post(
            '/apply/106',
            {
                'full_name': 'tester2',
                'email': 'tester2@email.com',
                'phone': 13234567,
                'linkedin': 'linkedin',
                'github_username': 'github',
                'why_company': 'test application',
                'why_role': 'test application',
                'why_you': 'test application',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            JobApplication.objects.filter(full_name='tester2').exists()
        )
    
    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.job.delete()
        

class TestDeleteJobApplication(TestCase):
    """
    Checks:
    1. Users can successfully delete their applications from db
    2. Users cannot delete other users' job applications.
    """

    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user1.save()

        self.user2 = User.objects.create(
            username='testuser102',
            password='hellotestuser102',
            email='tester2@email.com',
            id='102'
        )
        self.user2.save()

        self.job = JobPosting.objects.create(
            title='test job posting 101',
            posted_by=self.user1,
            salary=123456,
            location='London',
            closing_date="2025-05-05",
            company_overview="this is a test company",
            job_description="this is a test JD",
            requirements="These are test requirements",
            benefits="These are test benefits",
            approved=True,
            id='107'
        )
        self.job.save()

        self.application = JobApplication.objects.create(
            candidate=self.user2,
            job_posting=self.job,
            full_name=self.user2.username,
            email=self.user2.email,
            phone=12345678,
            linkedin='url.com',
            github_username='github',
            why_company="I like it",
            why_role='I like it',
            why_you='I like myself',
            id='108'
        )
        self.application.save()

    def test_delete_application(self):
        self.client.force_login(user=self.user2)
        response = self.client.post(reverse(
            'delete_application', kwargs={'application_id': '108'}
        ))
        self.assertRedirects(response, '/')
        self.assertFalse(
            JobApplication.objects.filter(id='108').exists()
        )

    def test_delete_other_users_application(self):
        self.client.force_login(user=self.user1)
        response = self.client.post(reverse(
            'delete_application', kwargs={'application_id': '108'}
        ))
        self.assertRedirects(response, '/')
        self.assertTrue(
            JobApplication.objects.filter(id='108').exists()
        )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.job.delete()
        self.application.delete()
