from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

User = settings.AUTH_USER_MODEL


class TimeStamp(models.Model):
    created_at = models.DateTimeField(_("create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


# class PermissionMixin(ModelViewSet):

#     def get_permissions(self):
#         if self.action == 'list':
#             return [AllowAny()]
#         elif self.action == 'retrieve':
#             return [AllowAny()]
#         elif self.action == 'create':
#             return [IsAuthenticated()]
#         elif self.action == 'update':
#             return [IsAuthenticated()]
#         elif self.action == 'partial_update':
#             return [IsAuthenticated()]
#         elif self.action == 'destroy':
#             return [IsAuthenticated()]
#         else:
#             return super().get_permissions()