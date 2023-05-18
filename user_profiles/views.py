from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import UserProfile
from .forms import AddUserProfileForm


class SeeAllProfiles(generic.ListView):
    """
    testclass
    """
    model = UserProfile
    queryset = UserProfile.objects.all()
    template_name = 'display_profiles.html'


class AddUserProfileDetails(generic.CreateView):
    """
    A class view to handle adding profile information
    once a user has signed up.
    """
    model = UserProfile
    form_class = AddUserProfileForm
    template_name = 'create_profile.html'

    def get_object(self, *args, **kwargs):
        return self.request.user.userprofile

    def post(self, request, *args, **kwargs):
        """
        A function to handle submitting user profile information
        to the database.
        """
        profile = AddUserProfileForm(data=request.POST)
        all_profiles = UserProfile.objects.all()

        if profile.is_valid():
            try:
                current_profile = get_object_or_404(
                    all_profiles, user=request.user)
                current_profile.delete()
            except UserProfile.DoesNotExist:
                pass
            profile.instance.user = request.user
            messages.success(request, 'PROFILE CREATED SUCCESSFULLY')
            profile.save()
            return redirect('home')
        else:
            messages.error(request,
                           'INVALID PROFILE DETAILS. PLEASE TRY AGAIN.')
            profile = AddUserProfileForm()
            return HttpResponseRedirect('add_user_profile_details')


class ViewProfile(View):
    """
    A class to handle users viewing their profile page. 
    """
    def get(self, request, *args, **kwargs):
        profles = UserProfile.objects.all()
        profile = get_object_or_404(profles, user=request.user)
        return render(
            request,
            'view_profile.html',
            {'profile': profile, }
        )


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
