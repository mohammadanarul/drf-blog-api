from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LikeModelViewset, LikeView

router = DefaultRouter()

router.register(r'likes', LikeModelViewset, basename='likes')

# urlpatterns = router.urls


urlpatterns = [
    path('liked/<slug>/', LikeView.as_view(), name='post_like_view')
    #     path('likes/', LikeCreateView.as_view(), name='post_like_view'),
    #     # path('post-likes', post_like_view, name='post_like_view'),
] + router.urls
