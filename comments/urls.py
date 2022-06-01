from django.urls import path
from .views import post_comments_list_api, PostCommentList

urlpatterns = [
    path('post/<slug>/', post_comments_list_api, name='post_commnet'),
    path('post-cm/<post>/', PostCommentList.as_view(), name='post_cm_commnet'),
]