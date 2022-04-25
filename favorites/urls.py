from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FavoriteModelViewSet

router = DefaultRouter()

router.register(r'favorites', FavoriteModelViewSet, basename='favorites')

urlpatterns = router.urls
