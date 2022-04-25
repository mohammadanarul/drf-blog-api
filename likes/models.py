from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
from posts.mixins import TimeStamp

User = get_user_model()


class Like(TimeStamp):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_like')
    liked = models.ManyToManyField(User, related_name='likes', blank=True)

    def all_like(self):
        return self.liked.count()

    def __str__(self):
        return f"{self.post.title}-{self.pk}"
