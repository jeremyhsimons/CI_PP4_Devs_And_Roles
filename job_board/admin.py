from django.contrib import admin
from .models import JobPosting
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(JobPosting)
class JobPostingAdmin(SummernoteModelAdmin):

    list_filter = ('approved', 'reported', 'created_on')
    list_display = ('title', 'created_on', 'approved', 'reported')
    search_fields = ['title', 'company_overview', 'job_description',
                    'requirements', 'benefits'
                    ]
