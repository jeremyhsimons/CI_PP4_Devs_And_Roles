from django import forms
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'summary', 'content', 'featured_image')


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'summary', 'content', 'featured_image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
