from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import mixins
from .models import Category
from .serializers import CategoryModelSerializer, CategorySerializer


class CategoryModelViewset(ModelViewSet):
    """
    TODO: Create, upadte, put, pacth
    A viewset for viewing and editing user instances.
    """
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'


class CategoryListView(mixins.CreateModelMixin, mixins.UpdateModelMixin, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
