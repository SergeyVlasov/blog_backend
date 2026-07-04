from django.db import models

from apps.posts.models import Post
from apps.users.models import User


class Comment(models.Model):
    text = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)