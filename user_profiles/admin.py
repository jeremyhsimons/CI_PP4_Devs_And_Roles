from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import UserProfile, Message


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    """
    A class handle user profile data management in the admin page.
    """
    list_display = ('first_name', 'last_name', 'user', 'created_on',
                    'approved', 'reported',)
    list_filter = ('approved', 'reported',)
    search_fields = ['first_name', 'last_name', 'user']
    actions = ['approve_profiles', 'disapprove_profiles', ]

    def approve_files(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_profiles(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Message)
class MessageAdmin(SummernoteModelAdmin):
    """
    A class handle message data management in the admin page.
    """
    list_display = ('recipient', 'first_name', 'last_name', 'sent_on')
    list_filter = ('recipient', 'sent_on')
    search_fields = [
        'recipient', 'first_name', 'last_name', 'email', 'message'
        ]
