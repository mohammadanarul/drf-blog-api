from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from posts.mixins import TimeStamp


class Category(TimeStamp, MPTTModel):
    name = models.CharField(_("name"), max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    slug = models.SlugField(_("slug"), unique=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
        # full_path = [self.name]
        # k = self.parent
        # while k is not None:
        #     full_path.append(k.name)
        #     k= k.parent
        # return '/'.join(full_path[::-1])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
