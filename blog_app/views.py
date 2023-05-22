from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import BlogPost, Comment
from .forms import BlogPostForm, UpdateBlogForm


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


class UpdateBlog(generic.UpdateView):
    """
    A class based view to handle users making edits to
    their blog posts on the site.
    """
    model = BlogPost
    form_class = UpdateBlogForm
    template_name = 'edit_blog.html'

    def get(self, request, slug, *args, **kwargs):
        blogs = BlogPost.objects.filter(approved=True)
        blog = get_object_or_404(blogs, slug=slug)
        updateform = UpdateBlogForm(
            initial={
                "title": blog.title,
                "summary": blog.summary,
                "content": blog.content,
                "featured_image": blog.featured_image,
            }
        )
        return render(
            request,
            'edit_blog.html',
            {
                'blog': blog,
                'form': updateform,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        updateblog_form = UpdateBlogForm(data=request.POST)

        if updateblog_form.is_valid():
            messages.success(request, 'BLOG POST UPDATED SUCCESSFULLY')
            updateblog_form.instance.posted_by = request.user
            updateblog_form.save()
        else:
            messages.error(
                request, 'PLEASE COMPLETE ALL FIELDS BEFORE SUBMITTING')
            updateblog_form = BlogPostForm()

        return render(
            request,
            'edit_blog.html'
        )


@login_required
def delete_blog(request, slug):
    blog = get_object_or_404(request, slug=slug)
    if request.user == blog.posted_by:
        messages.success(request, 'BLOG POST DELETED SUCCESSFULLY')
        blog.delete()
        HttpResponseRedirect(reverse('blog_list'))
    else:
        messages.error(
            request, 'YOU DO NOT HAVE PERMISSION TO DELETE THIS POST'
        )
        HttpResponseRedirect(reverse('blog_list'))
