from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import BlogPost, Comment
from .forms import BlogPostForm, UpdateBlogForm, CommentForm


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
        blogpost_form = BlogPostForm(request.POST, request.FILES)

        if blogpost_form.is_valid():
            print(blogpost_form.instance.featured_image)
            blogpost_form.instance.posted_by = request.user
            messages.success(
                request,
                'BLOG POST SUBMITTED SUCCESSFULLY.'
            )
            blogpost_form.save()
            return redirect('blog_list')
        else:
            messages.error(
                request,
                'BLOG POST NOT SUBMITTED. PLEASE COMPLETE ALL FIELDS.'
            )
            blogpost_form = BlogPostForm()
            return redirect('create_blog_post')


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
                'comments': comments,
                'form': CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        A method to handle comment submission
        """
        blog = get_object_or_404(BlogPost, slug=slug)
        comments = Comment.objects.filter(blog_post=blog).order_by(
            "created_on")
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid() and comment_form.instance.body != "":
            comment_form.instance.name = request.user.username
            comment_form.instance.blog_post = blog
            messages.success(request, 'YOUR COMMENT HAS BEEN POSTED.')
            comment_form.save()
        else:
            comment_form = CommentForm()
            messages.error(request, 'PLEASE SUBMIT A VALID COMMENT.')
            return redirect('blog_list')

        return render(
            request,
            'blog_post_detail.html',
            {
                'blog': blog,
                'comments': comments,
                'form': CommentForm(),
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
        blog = get_object_or_404(BlogPost, slug=slug)
        updateblog_form = UpdateBlogForm(
            request.POST, request.FILES, instance=blog
            )

        if updateblog_form.is_valid():
            updateblog_form.instance.posted_by = request.user
            updateblog_form.instance.slug = blog.slug
            updateblog_form.instance.created_on = blog.created_on
            messages.success(request, 'BLOG POST UPDATED SUCCESSFULLY')
            updateblog_form.save()
            return redirect('blog_list')
        else:
            messages.error(
                request, 'PLEASE COMPLETE ALL FIELDS BEFORE SUBMITTING')
            return render(
                request,
                'edit_blog.html',
                {
                    'blog': blog,
                    'form': updateblog_form,
                }
            )


@login_required
def delete_blog(request, slug):
    """
    A view to get and delete the specified
    blog if the author is the authorised user.
    """
    blog = get_object_or_404(BlogPost, slug=slug)
    if request.user == blog.posted_by:
        messages.success(request, 'BLOG POST DELETED SUCCESSFULLY')
        blog.delete()
        return HttpResponseRedirect(reverse('blog_list'))
    else:
        messages.error(
            request, 'YOU DO NOT HAVE PERMISSION TO DELETE THIS POST'
        )
        return HttpResponseRedirect(reverse('blog_list'))


@login_required
def delete_comment(request, comment_id):
    """
    A view to get and delete the specified
    comment if the author is the authorised user.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.username == comment.name:
        messages.success(request, 'COMMENT DELETED SUCCESSFULLY.')
        comment.delete()
        return HttpResponseRedirect(reverse_lazy('blog_list'))
    else:
        messages.error(
            request, 'YOU DO NOT HAVE PERMISSION TO DELETE THIS COMMENT')
        return HttpResponseRedirect(reverse_lazy('blog_list'))


@login_required
def report_blog(request, slug):
    """
    View that handles reporting of
    user profiles.
    """
    blog = get_object_or_404(BlogPost, slug=slug)
    if blog.reported is False and request.user != blog.posted_by:
        blog.reported = True
        blog.save()
        messages.success(
            request, "BLOG POST REPORTED. AN ADMIN WILL REVIEW IT"
            )
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request, "YOU CANNOT REPORT THIS BLOG POST")
        return HttpResponseRedirect(reverse('home'))


@login_required
def report_comment(request, pk):
    """
    View that handles reporting of
    user profiles.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if comment.reported is False:
        comment.reported = True
        comment.save()
        messages.success(
            request, "COMMENT REPORTED. AN ADMIN WILL REVIEW IT"
        )
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request, "YOU CANNOT REPORT THIS COMMENT")
        return HttpResponseRedirect(reverse('home'))
