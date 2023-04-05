from django.test import TestCase
from .forms import PostForm, ReviewForm
from .models import Post, Review


class TestPostForm(TestCase):
    def test_valid_form(self):
        data = {
            'title': 'Test post',
            'excerpt': 'This is a test post',
            'status': 'published',
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'title': '',
            'excerpt': 'This is a test post',
            'status': 'published',
        }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())


class TestReviewForm(TestCase):
    def test_valid_form(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'content': 'This is a test review',
        }
        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'email': 'john@example.com',
            'content': 'This is a test review',
        }
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())
