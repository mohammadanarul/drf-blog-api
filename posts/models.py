from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.utils.text import slugify
from category.models import Category
from django.contrib.auth import get_user_model
from .mixins import TimeStamp

User = get_user_model()


class Post(TimeStamp):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_post')
    title = models.CharField(_("title"), max_length=50)
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    description = models.TextField(_('description'))
    category = models.ForeignKey(Category, verbose_name=_(
        "category"), on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    tags = TaggableManager()
    status = models.CharField(
        _("status"), max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    # @property
    # def post_likes(self):
    #     return self.post_like
