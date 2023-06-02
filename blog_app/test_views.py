from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import BlogsList, BlogView
from .models import BlogPost


class TestBlogsList(TestCase):
    """
    Checks that a get request returns
    the correct response/template.
    """
    def test_get_blogs(self):
        response = self.client.get('/blog/blog_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')


class TestBlogView(TestCase):
    """
    Checks that a get request returns
    the correct blog page.
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.view = BlogView.as_view()
        self.user = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user.save()

        self.blog = BlogPost.objects.create(
            title='test-blog-one-o-one',
            slug='test-blog-101',
            posted_by=self.user,
            summary='a test blog',
            content='a test blog',
            id='202'
        )
        self.blog.save()

    def test_get_blog(self):
        # Checks that the url path for test blog works.
        self.client.force_login(self.user)
        request = self.factory.get('/blog/blog_detail/test-blog-101/')
        response = self.view(request, 'test-blog-101')
        self.assertEqual(response.status_code, 200)

    def test_post_comment(self):
        # Checks that comment submission results in 200 code.
        self.client.force_login(self.user)
        response = self.client.post(
            '/blog/blog_detail/test-blog-101',
            {
                'name': self.user.username,
                'body': 'this is a test comment',
                'blog_post': self.blog
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_post_invalid_comment(self):
        # Checks that comment submission results in 200 code.
        self.client.force_login(self.user)
        response = self.client.post(
            '/blog/blog_detail/test-blog-101',
            {
                'name': self.user.username,
                'body': '',
                'blog_post': self.blog
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/blog/blog_list/')

    def tearDown(self):
        self.user.delete()
        self.blog.delete()
