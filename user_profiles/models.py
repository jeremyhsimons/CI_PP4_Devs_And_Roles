from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model representing the user's public details
    displayed on their profile page.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200, blank=True)
    github_username = models.CharField(max_length=200, blank=True)
    job_seeker = models.BooleanField(default=False)
    recruiter = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True)
    years_experience = models.IntegerField()
    education = models.TextField()
    work_experience = models.TextField()
    interests = models.TextField()
    roles_open_to = models.CharField(max_length=200)
    approved = models.BooleanField(default=True)
    reported = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return (f"{self.first_name} {self.last_name}'s profile")
