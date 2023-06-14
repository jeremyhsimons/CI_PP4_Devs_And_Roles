from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ internal
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    A function to auto-create a profile for a new user.
    """
    if created:
        UserProfile.objects.create(user=instance)
