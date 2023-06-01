from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model representing the user's public details
    displayed on their profile page.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    github_username = models.CharField(max_length=200, blank=True)
    job_seeker = models.BooleanField(default=False)
    recruiter = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True)
    years_experience = models.IntegerField(null=True)
    education = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    roles_open_to = models.CharField(max_length=200, blank=True)
    approved = models.BooleanField(default=True)
    reported = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.user.username


class Message(models.Model):
    """
    A model representing the message that a recruiter can send
    to a job seeker through the site.
    """
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sent_on = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    message = models.TextField(blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return (
            f"{self.first_name}'s message to {self.recipient.first_name}")
