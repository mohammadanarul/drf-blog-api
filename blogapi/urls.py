from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# url routur config

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('category.urls')),
    path('', include('accounts.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('reports.urls'))
]
