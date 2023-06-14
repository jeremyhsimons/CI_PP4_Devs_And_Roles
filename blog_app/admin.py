# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd party
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import BlogPost, Comment


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    """
    A class to enable admin users to view and edit
    blog entries in the database.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'created_on', 'approved', 'reported')
    list_filter = ('created_on', 'approved', 'reported')
    search_fields = ['title', 'slug', 'summary', 'content']
    actions = ['approve_blog_post', 'disapprove_blog_post']

    def approve_blog_post(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_blog_post(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    A class to enable admin users to view and edit
    comments on blog posts.
    """
    list_display = ('name', 'body', 'blog_post', 'created_on',
                    'approved', 'reported')
    list_filter = ('approved', 'reported')
    search_fields = ('name', 'body')
    actions = ['approve_comment', 'disapprove_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_comment(self, request, queryset):
        queryset.update(approved=True)
