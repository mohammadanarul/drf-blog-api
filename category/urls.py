from django.urls import path
from .views import CategoryListView, ger_all_category_grouping

# app_name = 'category'
urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category'),
    path('test/', ger_all_category_grouping, name='cat')
]
