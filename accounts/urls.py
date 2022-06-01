from django.urls import path
from .views import AccountRegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register_view'),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
