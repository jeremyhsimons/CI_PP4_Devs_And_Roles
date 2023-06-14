# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd party
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View, generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import UserProfile, Message
from .forms import AddUserProfileForm, MessageUser


class SeeAllProfiles(generic.ListView):
    """
    A class based view to get all job seeker profiles
    and display them to a recruiter user.
    """
    model = UserProfile
    queryset = UserProfile.objects.filter(job_seeker=True)
    template_name = 'display_profiles.html'


class ProfileDetail(View, SuccessMessageMixin):
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
                'message_form': MessageUser(),
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = UserProfile.objects.filter(approved=True)
        profile = get_object_or_404(queryset, pk=pk)
        message_form = MessageUser(data=request.POST)

        if message_form.is_valid():
            message_form.instance.recipient = profile
            message_form.save()
            messages.success(request, 'MESSAGE SENT')
        else:
            message_form = MessageUser()
            messages.error(
                request, 'MESSAGE NOT SENT: PLEASE COMPLETE ALL FIELDS.'
                )
        return render(
            request,
            "profile_detail.html",
            {
                'profile': profile,
                'message_form': MessageUser(),
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
        profiles = UserProfile.objects.all()
        profile = get_object_or_404(profiles, user=request.user)
        user_messages = Message.objects.filter(
            recipient=profile).order_by('-sent_on')
        return render(
            request,
            'view_profile.html',
            {
                'profile': profile,
                'user_messages': user_messages,
            }
        )


class EditUserProfileDetails(generic.CreateView, SuccessMessageMixin):
    """
    A class view to handle adding profile information
    once a user has signed up.
    """
    model = UserProfile
    form_class = AddUserProfileForm
    template_name = 'edit_profile.html'

    def get(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(user=request.user)
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
        return render(
            request,
            'edit_profile.html',
            {'form': profile_form, }
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
            messages.success(request, 'PROFILE UPDATED SUCCESSFULLY')
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
    profile = get_object_or_404(profiles, user=request.user)

    if profile.user == request.user and profile.first_name:
        print("success")
        return redirect('home')
    else:
        print('fail')
        return redirect('add_user_profile_details')


@login_required
def report_profile(request, pk):
    """
    View that handles reporting of
    user profiles.
    """
    profile = get_object_or_404(UserProfile, pk=pk)
    if profile.reported is False and request.user != profile.user:
        profile.reported = True
        profile.save()
        messages.success(request, "PROFILE REPORTED. AN ADMIN WILL REVIEW IT")
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request, "YOU CANNOT REPORT THIS PROFILE")
        return HttpResponseRedirect(reverse('home'))
