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
]