from django.test import TestCase
from .forms import PostForm, ReviewForm


class TestPostForm(TestCase):

    def test_post_name_is_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def field_is_not_required(self):
        form = PostForm({'title': 'Test Posts'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(
            form.Meta.fields, ['title', 'excerpt', 'image', 'status'])
    

class TestReviewForm(TestCase):

    def test_review_name_is_required(self):
        form = ReviewForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('nmae', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def field_is_not_required(self):
        form = ReviewForm({'name': 'Test Reviews'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(
            form.Meta.fields, ['name', 'email', 'content'])
    
