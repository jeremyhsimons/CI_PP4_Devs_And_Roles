from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import UserProfile
from .forms import AddUserProfileForm


class SeeAllProfiles(generic.ListView):
    """
    testclass
    """
    model = UserProfile
    queryset = UserProfile.objects.all()
    template_name = 'display_profiles.html'


class AddUserProfileDetails(generic.UpdateView):
    """
    A class view to handle adding profile information
    once a user has signed up.
    """
    model = UserProfile
    form_class = AddUserProfileForm
    template_name = 'create_profile.html'

    def get_object(self, *args, **kwargs):
        return self.request.user.userprofile


    # model = UserProfile
    # form_class = AddUserProfileForm
    # template_name = "create_profile.html"

    # def get_object(self):
    #     return self.request.user

    # def form_invalid(self, form):
    #     return redirect('home')


def redirect_view(request):
    """
    view that redirects users to set up
    profile if they have not done so.
    """
    profiles = UserProfile.objects.all()
    current_user_profile = get_object_or_404(profiles, user=request.user)

    if current_user_profile.user == request.user and current_user_profile.first_name:
        print("success")
        return redirect('home')
    else:
        print('fail')
        return redirect('add_user_profile_details')
