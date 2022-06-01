from django.urls import path
from .views import PostDetailAPIView, PostCreateApi



urlpatterns = [
    path('post-detail/<slug>/', PostDetailAPIView.as_view(), name='post_detail_api'),
    path('create/', PostCreateApi.as_view(), name='post_create_api')
    # path('category-posts/<slug>/', recent_post_filter, name='category-posts')
]
