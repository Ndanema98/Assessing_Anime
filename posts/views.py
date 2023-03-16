from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Review
from .forms import PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("date_posted")
    template_name = "index.html"
    context_object_name = 'post_list'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        reviews = post.reviews.filter(approved=True).order_by('date_posted')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
            }
        )


def post(request):
    return HttpResponse('Post view')


def review(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
    }
    
    return render(request, 'post_detail.html', context)


def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:PostList')

    return render(request, 'post_form.html', {'form': form})


def update_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('posts:PostList')

    return render(request, 'post_form.html', {'form': form, 'post': post})
    

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:PostList')
    return render(request, 'post_delete.html', {'post': post})