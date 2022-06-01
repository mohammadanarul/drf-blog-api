from django.urls import path
from .views import LikeAPIView


urlpatterns = [
    path('liked/<slug>/', LikeAPIView.as_view(), name='post_like_view')
]
