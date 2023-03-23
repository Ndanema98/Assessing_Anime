from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Review


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = User.objects.create(username='testuser')
        Post.objects.create(title='Test Post', slug='test-post', description='This is a test post', author=author)

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_excerpt_blank(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.excerpt, '')

    def test_number_of_likes(self):
        post = Post.objects.get(id=1)
        user = User.objects.create(username='testuser2')
        post.upvotes.add(user)
        self.assertEquals(post.number_of_likes(), 1)

    def test_number_of_dislikes(self):
        post = Post.objects.get(id=1)
        user = User.objects.create(username='testuser3')
        post.downvotes.add(user)
        self.assertEquals(post.number_of_dislikes(), 1)


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(
            username='testuser', password='password'
        )

        testpost = Post.objects.create(
            title='Test Post',
            description='This is a test post',
            author=testuser,
            excerpt='This is a test excerpt',
        )
        
        testreview = Review.objects.create(
            post=testpost,
            name='Test Name',
            author=testuser,
            email='test@example.com',
            content='This is a test review',
        )
        
    def test_content(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.content, 'This is a test review')
     
    def test_approved_default(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.approved, False)