from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostModelViewset, recent_post_filter

router = DefaultRouter()
router.register(r'posts', PostModelViewset, basename='posts')


urlpatterns = [
    path('recent-posts/<category>/', recent_post_filter, name='recent-posts')
] + router.urls
