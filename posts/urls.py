from . import views
from django.urls import path

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='PostList'),
    path('post/', views.post, name='post'),
    path('<int:post_id>', views.review, name='review'),
    path('add/', views.create_post, name='create_post'),
    path('update/<int:post_id>', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:post_id>/create_review/', views.create_review, name='create_review'),
    path('like/<int:post_id>', views.PostLike.as_view(), name='post_like'),
    path('dislike/<int:post_id>', views.PostDislike.as_view(), name='post_dislike'),


] 