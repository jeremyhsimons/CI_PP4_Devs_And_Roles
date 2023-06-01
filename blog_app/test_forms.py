from django.test import TestCase
from django.contrib.auth.models import User
from .forms import BlogPostForm, CommentForm, UpdateBlogForm
from .models import BlogPost


class TestBlogPostForm(TestCase):
    """
    A class to test the blog post form
    functions as expected.
    """
    def test_required_fields(self):
        required_fields = ['title', 'slug', 'summary', 'content',]
        for field in required_fields:
            form = BlogPostForm({field: ''})
            self.assertFalse(form.is_valid())
    
    def setUp(self):
        """
        Save a new blog to the db
        """
        self.user = User.objects.create(username="Henry")
        self.blog = BlogPost.objects.create(
            title='This is a brand new test blog',
            slug='brand-new-test',
            posted_by=self.user
        )
        self.blog.save()

    def test_unique_fields(self):
        """
        Try to create a blog with the same title and slug.
        """
        form = BlogPostForm({
            'title': 'This is a brand new test blog',
            'slug': 'brand-new-test',
        })
        self.assertFalse(form.is_valid())

    def tearDown(self):
        """
        Destroy the blog after test runs
        """
        self.blog.delete()


class TestUpdateBlogForm(TestCase):
    """
    A class to check users can't submit empty
    required fields to update blog form.
    """
    def test_required_fields(self):
        """
        Loop through fields and test them as empty.
        """
        required_fields = ['title', 'summary', 'content',]
        for field in required_fields:
            form = UpdateBlogForm({field: ''})
            self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    """
    A class to check users can't submit empty comment.
    """
    def test_empty_comment(self):
        form = CommentForm({'body':''})
        self.assertFalse(form.is_valid())
