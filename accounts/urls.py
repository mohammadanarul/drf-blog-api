from unicodedata import name
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AccountModelViewset, AccountRegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', AccountModelViewset, basename='users')

urlpatterns = [
    path('accounts-create', AccountRegisterView.as_view(), name='accounts-create'),
    path('accounts/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('accounts/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
