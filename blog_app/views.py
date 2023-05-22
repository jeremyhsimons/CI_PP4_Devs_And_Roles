from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import BlogPost, Comment
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


class BlogView(View):
    """
    A class based view to handle viewing blog posts.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Method to get the blog post content and comments for
        display in the detail page.
        """
        blogs = BlogPost.objects.filter(approved=True)
        blog = get_object_or_404(blogs, slug=slug)
        comments = Comment.objects.filter(blog_post=blog).order_by(
            "created_on")
        return render(
            request,
            'blog_post_detail.html',
            {
                'blog': blog,
                'comments': comments
            }
        )
