from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("date_posted")
    template_name = "index.html"
    paginate_by = 4



# Create your views here.
