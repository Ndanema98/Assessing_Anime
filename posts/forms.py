from django import forms
from .models import Post, Review


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'image', 'status']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'content']