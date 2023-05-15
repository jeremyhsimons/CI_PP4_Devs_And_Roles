from django.contrib import admin
from .models import JobPosting, JobApplication
from django_summernote.admin import SummernoteModelAdmin


@admin.register(JobPosting)
class JobPostingAdmin(SummernoteModelAdmin):

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

    list_filter = ('candidate', 'job_posting',)
    list_display = ('candidate', 'full_name', 'created_on')
    search_fields = ['full_name',]
