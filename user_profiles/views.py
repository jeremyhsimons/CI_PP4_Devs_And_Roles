from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import UserProfile
from .forms import AddUserProfileForm


class SeeAllProfiles(generic.ListView):
    """
    A class based view to get all job seeker profiles
    and display them to a recruiter user.
    """
    model = UserProfile
    queryset = UserProfile.objects.filter(job_seeker=True)
    template_name = 'display_profiles.html'


class ProfileDetail(View):
    """
    A class to view the details of a job seeker's profile
    """

    def get(self, request, pk, *args, **kwargs):
        queryset = UserProfile.objects.filter(approved=True)
        profile = get_object_or_404(queryset, pk=pk)

        return render(
            request,
            "profile_detail.html",
            {
                'profile': profile,
            },
        )


class AddUserProfileDetails(generic.CreateView, SuccessMessageMixin):
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


class EditUserProfileDetails(generic.CreateView, SuccessMessageMixin):
    """
    A class view to handle adding profile information
    once a user has signed up.
    """
    model = UserProfile
    form_class = AddUserProfileForm
    template_name = 'edit_profile.html'

    def get_object(self, *args, **kwargs):
        profile = self.request.user.userprofile
        profile_form = AddUserProfileForm(
            initial={
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'linkedin': profile.linkedin,
                'github_username': profile.github_username,
                'job_seeker': profile.job_seeker,
                'recruiter': profile.recruiter,
                'location': profile.location,
                'years_experience': profile.years_experience,
                'education': profile.education,
                'work_experience': profile.work_experience,
                'interests': profile.interests,
                'roles_open_to': profile.roles_open_to,
            }
        )

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


class DeleteProfile(generic.DeleteView):
    """
    A view to handle the deletion of users' profiles.
    """
    model = User
    template_name = 'delete_profile.html'

    def get_object(self, *args, **kwargs):
        return self.request.user

    def post(self, request, *args, **kwargs):
        if UserProfile.objects.filter(user=request.user).exists():
            profile = UserProfile.objects.filter(user=request.user)
            profile.delete()

        request.user.is_active = False
        request.user.save()
        messages.success(request, 'YOUR ACCOUNT WAS SUCCESSFULLY DELETED')

        return HttpResponseRedirect(reverse_lazy('account_logout'))


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
