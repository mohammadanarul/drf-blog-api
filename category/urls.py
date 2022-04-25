from unicodedata import name
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewset, CategoryListView

router = DefaultRouter()
router.register(r'categories', CategoryModelViewset, basename='categories')

# app_name = 'category'
urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category')
] + router.urls
