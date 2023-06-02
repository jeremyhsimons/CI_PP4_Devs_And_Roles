from django.test import TestCase, RequestFactory
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal imports
from .views import BlogsList, BlogView, WriteBlog, UpdateBlog
from .models import BlogPost, Comment


class TestBlogsList(TestCase):
    """
    Checks that a get request returns
    the correct response/template.
    """
    def test_get_blogs(self):
        response = self.client.get('/blog/blog_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')


class TestWriteBlog(TestCase):
    """
    Checks that submitting a blog form
    returns the correct response.
    """
    def setUp(self):
        self.user = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user.save()

    def test_get_blog_form(self):
        response = self.client.get('/blog/create_blog_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'create_blog_post.html'
            )

    def test_submit_blog_form(self):
        # User authentication required
        self.client.force_login(self.user)
        # submitting a new blog
        response = self.client.post(
            '/blog/create_blog_post/',
            {
                'title': 'test blog',
                'slug': 'test-blog-1',
                'content': 'This is a test submission',
                'summary': 'This is a test submission',
            }
        )
        self.assertEqual(response.status_code, 200)
        # blog exists in the db.
        self.assertTrue(
            BlogPost.objects.filter(slug='test-blog-1').exists()
            )

    def test_submit_invalid_blog_form(self):
        # User authentication required
        self.client.force_login(self.user)
        # submitting a new blog
        self.client.post(
            '/blog/create_blog_post/',
            {
                'title': '',
                'slug': 'faulty-submission-test',
                'content': '',
                'summary': '',
            }
        )
        # blog doesn't exist in the db.
        self.assertFalse(
            BlogPost.objects.filter(slug='faulty-submission-test').exists()
        )


class TestUpdateBlog(TestCase):
    """
    A class to check that the updateblog view:
    1. gets the correct blog content from the db.
    2. saves valid updated form data to db.
    3. does not save invalid form data to the db.
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user1.save()

        self.blog1 = BlogPost.objects.create(
            title='test-blog-one-o-one',
            slug='test-blog-101',
            posted_by=self.user1,
            summary='a test blog',
            content='a test blog',
        )
        self.blog1.save()

    def test_get_blog_data(self):
        response = self.client.get('/blog/edit_blog/test-blog-101')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_blog.html')

    def test_submit_edited_blog(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            '/blog/edit_blog/test-blog-101',
            {
                'title': ' updated',
                'content': 'updated',
                'summary': 'updated',
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(BlogPost.objects.filter(title='updated').exists())

    def test_invalid_submission_blog_edits(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            '/blog/edit_blog/test-blog-101',
            {
                'title': '',
                'content': '',
                'summary': '',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(BlogPost.objects.filter(title='').exists())

    def tearDown(self):
        self.user1.delete()
        self.blog1.delete()




class TestBlogView(TestCase):
    """
    Checks that the testblog view:
    1. returns the correct data when getting the blog.
    2. returns a 200 status code when valid comment is submitted.
    3. returns a 302 status code when invalid comment is submitted.
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


class TestDeleteBlog(TestCase):
    """
    Checks to see if a user can successfully delete their blog post
    and that users cannot delete another person's blog post
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user1.save()

        self.user2 = User.objects.create(
            username='testuser102',
            password='hellotestuser102',
            email='tester2@email.com',
            id='102'
        )
        self.user2.save()

        self.blog1 = BlogPost.objects.create(
            title='test-blog-one-o-one',
            slug='test-blog-101',
            posted_by=self.user1,
            summary='a test blog',
            content='a test blog',
        )
        self.blog1.save()

        self.blog2 = BlogPost.objects.create(
            title='test-blog-one-o-two',
            slug='test-blog-102',
            posted_by=self.user1,
            summary='another test blog',
            content='another test blog',
        )
        self.blog2.save()

    def test_delete_blog(self):
        # user deletes their own blog post.
        self.client.force_login(self.user1)
        response = self.client.post(reverse(
            'delete_blog', kwargs={'slug': self.blog1.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            BlogPost.objects.filter(slug=self.blog1.slug).exists()
            )
        
    def test_delete_other_user_blog(self):
        # user tries to delete another user's blog.
        self.client.force_login(self.user2)
        response = self.client.post(reverse(
            'delete_blog', kwargs={'slug': self.blog2.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            BlogPost.objects.filter(slug=self.blog2.slug).exists()
            )

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.blog1.delete()
        self.blog2.delete()




class TestDeleteComment(TestCase):
    """
    Checks if the user can delete comment,
    and if user is restricted from deleting comment.
    """
    def setUp(self):
        self.user1 = User.objects.create(
            username='testuser101',
            password='hellotestuser101',
            email='tester@email.com',
            id='101'
        )
        self.user1.save()

        self.user2 = User.objects.create(
            username='testuser102',
            password='hellotestuser102',
            email='tester2@email.com',
            id='102'
        )
        self.user2.save()

        self.blog = BlogPost.objects.create(
            title='test-blog-one-o-one',
            slug='test-blog-101',
            posted_by=self.user1,
            summary='a test blog',
            content='a test blog',
        )
        self.blog.save()

        self.comment1 = Comment.objects.create(
            name=self.user2.username,
            body='this is a test comment that I regret posting',
            blog_post=self.blog,
            id='103'
        )

        self.comment2 = Comment.objects.create(
            name=self.user2.username,
            body='this is another test comment that I regret posting',
            blog_post=self.blog,
            id='104'
        )

    def test_delete_comment(self):
        # check deleting comment works and removes instance from db
        self.client.force_login(self.user2)
        response = self.client.post(reverse(
            'delete_comment', kwargs={'comment_id': self.comment1.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(pk=self.comment1.id).exists())

    def test_delete_other_user_comment(self):
        # check that user cannot delete another user's comment.
        self.client.force_login(self.user1)
        response = self.client.post(reverse(
            'delete_comment', kwargs={'comment_id': self.comment2.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(pk=self.comment2.id).exists())

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.blog.delete()
