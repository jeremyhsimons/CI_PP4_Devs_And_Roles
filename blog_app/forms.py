from django import forms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    """
    A class to package model data and labels to the create blog form page
    """
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'summary', 'content', 'featured_image',)
        labels = {
            'title': 'Blog Title',
            'slug': 'Unique ID: Can only  contain letters, hyphens, numbers or underscores',
            'summary': 'Blog Summary',
            'content': 'Blog Content',
            'featured': 'Add an image for your blog post (optional)',
        }


class UpdateBlogForm(forms.ModelForm):
    """
    A class to package model data and labels to the update blog form page
    """
    class Meta:
        model = BlogPost
        fields = ('title', 'summary', 'content', 'featured_image',)
        labels = {
            'title': 'Blog Title',
            'summary': 'Blog Summary',
            'content': 'Blog Content',
            'featured': 'Add an image for your blog post (optional)',
        }


class CommentForm(forms.ModelForm):
    """
    A class to package model data and labels to the blog detail/comment form.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Write your comment here.',
        }
