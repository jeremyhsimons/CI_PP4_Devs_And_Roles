from django.shortcuts import render
from django.views import generic, View
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import BlogPost
from .forms import BlogPostForm


class BlogsList(generic.ListView):
    """
    A class-based view to handle the display of six posts
    per page on desktop, and fewer for smaller devices.
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(approved=True).order_by('created_on')
    template_name = "blog.html"
    paginate_by = 6


class WriteBlog(generic.CreateView):
    """
    A class-based view to allow users
    to create their own blog posts.
    """
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create_blog_post.html'

    def post(self, request, *args, **kwargs):
        blogpost_form = BlogPostForm(data=request.POST)

        if blogpost_form.is_valid():
            blogpost_form.instance.posted_by = request.user
            blogpost_form.save()
        else:
            blogpost_form = BlogPostForm()

        return render(
            request,
            'create_blog_post.html'
        )
