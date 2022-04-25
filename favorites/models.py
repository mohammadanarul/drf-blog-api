from django.db import models
from posts.models import Post
from posts.mixins import TimeStamp
from django.contrib.auth import get_user_model

User = get_user_model()


class Favorite(TimeStamp):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_favorites')
    user = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='favorites')
