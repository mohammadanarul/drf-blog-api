from django.db import models
from django.utils.translation import gettext_lazy as _
from posts.models import Post
from posts.mixins import TimeStamp
from django.contrib.auth import get_user_model

User = get_user_model()

'''
SPAM
HARMASSMENT
RULESVIOLATION
SPAM = 1
HARMASSMENT = 2
RULESVIOLATION = 3
'''


class PostReport(TimeStamp):
    STATUS = (
        ('Spam', 'Spam'),
        ('Harassment', 'Harassment'),
        ('Rules Violation', 'Rules Violation')
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_report')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_report')
    body = models.TextField(help_text=_("post report content"), max_length=500)
    status = models.CharField(max_length=15, choices=STATUS, default='Spam')

    def __str__(self):
        return f"{self.post.title}->{self.user.username}"

    class Meta:
        ordering = ['-created_at']
