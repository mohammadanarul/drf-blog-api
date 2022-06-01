from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins, response, status
from .models import Category
from .serializers import CategoryModelSerializer, CategorySerializer


class CategoryModelViewset(ModelViewSet):
    """
    TODO: Create, upadte, put, pacth
    A viewset for viewing and editing user instances.
    """
    queryset = Category.objects.root_nodes()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'


class CategoryListView(mixins.CreateModelMixin, mixins.UpdateModelMixin, generics.ListAPIView):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer


def ger_all_category_grouping(request):
    try:
        category = Category.objects.get(slug='Django')
        full_category = category.get_ancestors(include_self=True)
        return response.Response({
            'messages': 'successfully completed your recursive function',
            'data': full_category.data
        })
    except Exception as e:
        return print(f"awesome:  {e}")

