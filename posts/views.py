from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Review
from .forms import PostForm, ReviewForm


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.post = Post.objects.create(
            title='Test post',
            content='This is a test post content',
            author=self.user,
            status=1
        )
        self.review = Review.objects.create(
            content='This is a test review content',
            author=self.user,
            post=self.post
        )
        self.post_like_url = reverse('posts:like', args=[self.post.id])
        self.post_dislike_url = reverse('posts:dislike', args=[self.post.id])
        self.post_list_url = reverse('posts:PostList')
        self.post_create_url = reverse('posts:create_post')
        self.post_update_url = reverse('posts:update_post', args=[self.post.id])
        self.post_delete_url = reverse('posts:delete_post', args=[self.post.id])
        self.post_review_url = reverse('posts:review', args=[self.post.id])
        self.post_review_create_url = reverse('posts:create_review', args=[self.post.id])

    def test_post_list_view(self):
        response = self.client.get(self.post_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.post_create_url, {
            'title': 'New post',
            'content': 'This is a new post content',
        })
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.post_list_url)

    def test_post_update_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.post_update_url, {
            'title': 'Updated post',
            'content': 'This is an updated post content',
        })
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.post_list_url)

    def test_post_delete_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.post_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.post_list_url)

    def test_post_like_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.post_like_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.post_review_url)





