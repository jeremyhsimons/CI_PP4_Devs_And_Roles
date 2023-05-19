from django import forms
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'summary', 'content', 'featured_image')
