from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from posts.models import Post
from posts.mixins import TimeStamp


class Comment(TimeStamp, MPTTModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_("user"),
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    publish = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['-created_at']

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f'Comment by {self.user.username}'

    def get_absolute_url(self):
        return reverse('blog:single_post_view', kwargs={'slug': self.post.slug})
