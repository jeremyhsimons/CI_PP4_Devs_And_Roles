from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name', 'user', 'created_on',
                    'approved', 'reported',)
    list_filter = ('approved', 'reported',)
    search_fields = ['first_name', 'last_name', 'user']
    actions = ['approve_profiles', 'disapprove_profiles',]

    def approve_files(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_profiles(self, request, queryset):
        queryset.update(approved=False)
