from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import JobPosting, JobApplication


@admin.register(JobPosting)
class JobPostingAdmin(SummernoteModelAdmin):
    """
    A class to handle management of jobposting data on admin page.
    """
    list_filter = ('approved', 'reported', 'created_on')
    list_display = ('title', 'created_on', 'approved', 'reported')
    search_fields = ['title', 'company_overview', 'job_description',
                     'requirements', 'benefits']
    actions = ['approve_job_posting', 'disapprove_job_posting']

    def approve_job_posting(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_job_posting(self, request, queryset):
        queryset.update(approved=False)


@admin.register(JobApplication)
class JobApplicationAdmin(SummernoteModelAdmin):
    """
    A class to handle management of jobapplication data on admin page.
    """
    list_filter = ('candidate', 'job_posting',)
    list_display = ('candidate', 'full_name', 'created_on')
    search_fields = ['full_name', ]
