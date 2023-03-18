from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Review
from .forms import PostForm, ReviewForm


class PostLike(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('posts:review', args=[post.id]))


class PostDislike(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        if post.downvotes.filter(id=request.user.id).exists():
            post.downvotes.remove(request.user)
        else:
            post.downvotes.add(request.user)

        return HttpResponseRedirect(reverse('posts:review', args=[post.id]))


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("date_posted")
    template_name = "index.html"
    context_object_name = 'post_list'
    paginate_by = 3


def post(request):
    return HttpResponse('Post view')


def review(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
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

    if post.author != request.user:
        messages.error(request, "You don't have permission to delete the post")
        return redirect('posts:PostDetail', post_id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts:PostList')
    return render(request, 'post_delete.html', {'post': post})


def create_review(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    reviewform = ReviewForm()
    if request.method == 'POST':
        reviewform = ReviewForm(request.POST)
        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.author = request.user
            review.post = post
            review.save()
            return redirect('posts:review', post_id=post_id)
    return render(request, 'review_form.html', {'reviewform': reviewform, 'post': post})



