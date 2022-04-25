from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostReportModelViewset

router = DefaultRouter()
router.register(r'reports', PostReportModelViewset, basename='reports')

urlpatterns = router.urls
