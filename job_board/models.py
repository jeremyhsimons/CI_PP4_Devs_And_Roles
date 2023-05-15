from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class JobPosting(models.Model):
    """
    A model to outline the data required
    for each job posting on the site.
    """
    title = models.CharField(max_length=200, unique=False)
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_posting"
    )
    salary = models.IntegerField()
    location = models.CharField(max_length=200)
    closing_date = models.DateTimeField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    company_overview = models.TextField(unique=True)
    job_description = models.TextField(unique=True)
    requirements = models.TextField(unique=True)
    benefits = models.TextField(unique=True)
    applicants = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    reported = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_applicants(self):
        return self.applicants.count()

    def get_deadline(self):
        return self.closing_date


class JobApplication(models.Model):
    """
    A class to represent the data required in a
    job application to one of the postings
    on the site.
    """
    candidate = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_application"
    )
    job_posting = models.ForeignKey(
        JobPosting, on_delete=models.CASCADE, related_name="job_application"
    )
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(max_length=20)
    linkedin = models.CharField(max_length=200)
    github_username = models.CharField(max_length=200)
    why_company = models.TextField(max_length=2000)
    why_role = models.TextField(max_length=2000)
    why_you = models.TextField(max_length=2000)
    supporting_docs = models.FileField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.pk
