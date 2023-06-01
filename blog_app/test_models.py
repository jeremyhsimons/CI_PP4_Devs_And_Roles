from django.test import TestCase
from django.contrib.auth.models import User 
from .models import BlogPost, Comment


class TestBlogPost(TestCase):
    """
    Checks str method works correctly
    """
    def test_string_method(self):
        user = User.objects.create(username="Francesca")
        blog = BlogPost.objects.create(
            title='This is yet another test blog',
            slug='another-test-12345',
            posted_by=user
        )
        self.assertEqual(str(blog), 'This is yet another test blog')



class TestComment(TestCase):
    """
    Checks str method works correctly
    """
    def test_string_method(self):
        user1 = User.objects.create(username="Mary")
        user2 = User.objects.create(username="Martha")
        blog = BlogPost.objects.create(
            title='How to avoid burnout',
            slug='avoid-burnout-123',
            posted_by=user1 
        )
        comment = Comment.objects.create(
            name=user2.username,
            body="This is really helpful!",
            blog_post=blog,
        )
        self.assertEqual(
            str(comment), "Martha's comment on How to avoid burnout."
            )
