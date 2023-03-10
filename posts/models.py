from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="anime_posts"
    )
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        ordering = ["date_posted"]

    def __str__(self):
        return self.title


class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=80, default="Anonymous")
    email = models.EmailField(default="example@example.com")
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Review for {self.post.title}'
