from django.db import models
from django.contrib.auth.models import User


class ContactMessage(models.Model):
    """
    A class representing the data sent to the db
    when a user submits a contact form to the site.
    """
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,
        blank=True, related_name='contact_message')
    date_sent = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_sent']

    def __str__(self):
        return (f'{self.pk}-{self.full_name}')
