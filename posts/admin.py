from django.contrib import admin
from .models import Post, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'date_posted','author')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_posted')
    summernote_fields = ('description')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = (
        'name', 'content', 'post', 'date_posted', 'approved', 'author')
    list_filter = ('approved', 'date_posted')
    search_fields = ['name', 'email', 'content']
    summernote_fields = ('content')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


