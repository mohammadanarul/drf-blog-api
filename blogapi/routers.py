from rest_framework.routers import DefaultRouter
from accounts.views import AccountModelViewset
from posts.views import PostModelViewset
from comments.views import CommentViewSet
from category.views import CategoryModelViewset
from reports.views import PostReportModelViewset
from likes.views import LikeModelViewset
from favorites.views import FavoriteModelViewSet

# url routur config
router = DefaultRouter()
router.register(r'accounts', AccountModelViewset, basename='accounts')
router.register(r'categories', CategoryModelViewset, basename='categories')
router.register(r'posts', PostModelViewset, basename='posts')
router.register(r'likes', LikeModelViewset, basename='likes')
router.register(r'favorites', FavoriteModelViewSet, basename='favorites')
router.register(r'reports', PostReportModelViewset, basename='reports')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls