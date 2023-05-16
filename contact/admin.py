from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(SummernoteModelAdmin):
    list_display = ('full_name', 'date_sent', 'user', 'read')
    list_filter = ('date_sent', 'read')
    search_fields = ['full_name', 'message',]
    actions = ['mark_as_read',]

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
