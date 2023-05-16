from django.shortcuts import render, redirect
from django.views import View, generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import UserProfile
from .forms import AddUserProfileForm


class AddUserProfileDetails(generic.UpdateView):
    """
    A class view to handle adding profile information
    once a user has signed up.
    """
    model = UserProfile
    form_class = AddUserProfileForm
    template_name = "create_profile.html"


def redirect_view(request):
    """
    view that redirects users to set up
    profile if they have not done so.
    """

    if request.user.userprofile:
        print("success")
        return redirect('home')
    else:
        print('fail')
        return redirect('add_user_profile_details')
