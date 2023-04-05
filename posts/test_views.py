from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from posts.models import Post, Review
from posts.forms import PostForm, ReviewForm


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            status=1,
            author=self.user,
        )
        self.review = Review.objects.create(
            title='Test Review',
            content='Test Content',
            rating=3,
            author=self.user,
            post=self.post,
        )

    def test_PostList_GET(self):
        response = self.client.get(reverse('posts:PostList'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_create_post_POST(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse('posts:create_post'), {
            'title': 'New Test Post',
            'content': 'New Test Content',
        })

        self.assertRedirects(response, reverse('posts:PostList'))
        self.assertTrue(Post.objects.filter(title='New Test Post').exists())

    def test_create_review_POST(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse(
            'posts:create_review', args=[self.post.id]), {
            'title': 'New Test Review',
            'content': 'New Test Content',
            'rating': 4,
        })

        self.assertRedirects(response, reverse(
            'posts:review', args=[self.post.id]))
        self.assertTrue(Review.objects.filter(
            title='New Test Review').exists())

    def test_update_post_POST(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse(
            'posts:update_post', args=[self.post.id]), {
            'title': 'Updated Test Post',
            'content': 'Updated Test Content',
        })

        self.assertRedirects(response, reverse('posts:PostList'))
        self.post.refresh_from_db()
        self.assertEquals(self.post.title, 'Updated Test Post')
        self.assertEquals(self.post.content, 'Updated Test Content')

    def test_delete_post_POST(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse(
            'posts:delete_post', args=[self.post.id]))

        self.assertRedirects(response, reverse('posts:PostList'))
        self.assertFalse(Post.objects.filter(title='Test Post').exists())

    def test_PostLike_POST(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse(
            'posts:PostLike', args=[self.post.id]))

        self.assertRedirects(response, reverse(
            'posts:review', args=[self.post.id]))
        self.assertEquals(self.post.upvotes.count(), 1)
        self.assertTrue(self.post.upvotes.filter(id=self.user.id).exists())

    def test_PostDislike_POST(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse(
            'posts:PostDislike', args=[self.post.id]))

        self.assertRedirects(response, reverse(
            'posts:review', args=[self.post.id]))
        self.assertEquals(self.post.downvotes.count(), 1)
        self.assertTrue(self.post.downvotes.filter(id=self.user.id).exists())
