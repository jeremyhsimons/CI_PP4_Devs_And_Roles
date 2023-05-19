from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class BlogPost(models.Model):
    """
    A class to represent the data required for each
    blog entry to the site.
    """
    title = models.CharField(max_length=200, unique=True)
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog')
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    summary = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    reported = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A class to represent the data needed for each
    comment on a blog post.
    """
    name = models.CharField(max_length=80)
    body = models.TextField()
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comment')
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    reported = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.name}'s comment on {self.blog_post}."
