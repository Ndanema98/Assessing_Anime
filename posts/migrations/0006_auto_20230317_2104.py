# Generated by Django 3.2.18 on 2023-03-17 21:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_alter_review_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvotes',
        ),
        migrations.AddField(
            model_name='post',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='post_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]