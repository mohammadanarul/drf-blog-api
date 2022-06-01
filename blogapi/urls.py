from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="DRF BLOG API",
      default_version='v1',
      description="testing and productions",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mdanarul7075@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/', include('posts.urls')),
    path('api/v1/', include('comments.urls')),
    path('api/v1/', include('likes.urls')),
    path('api/v1/', include('category.urls')),
    path('api/v1/', include('blogapi.routers')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



# path('swagger-ui/', TemplateView.as_view(
#     template_name='swagger-ui.html',
#     extra_context={'schema_url':'openapi-schema'}
# ), name='swagger-ui'),
# path('docs/', TemplateView.as_view(
#     template_name='docs.html',
#     extra_context={'schema_url':'api_schema'}
#     ), name='swagger-ui'),