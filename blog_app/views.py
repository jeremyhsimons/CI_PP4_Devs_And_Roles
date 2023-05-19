from django.shortcuts import render
from django.views import generic, View
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import BlogPost


class BlogsList(generic.ListView):
    """
    A class-based view to handle the display of six posts
    per page on desktop, and fewer for smaller devices.
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(approved=True).order_by('created_on')
    template_name = "blog.html"
    paginate_by = 6
