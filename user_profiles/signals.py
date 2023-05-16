from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# internal
from .models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.created(user=instance)
