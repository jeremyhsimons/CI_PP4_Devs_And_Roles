from .models import UserProfile


def profiles_context(request):
    """
    Makes user profile objects accessible in all views.
    """
    profiles = UserProfile.objects.all()
    return {'userprofiles': profiles}