from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from category.models import Category
from .serializers import PostSerializer, PostDetailSerializer

class PostCreateApi(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostModelViewset(ModelViewSet):
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        elif self.action == 'retrieve':
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'update':
            return [IsAuthenticated()]
        elif self.action == 'partial_update':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsAuthenticated()]
        else:
            return super(PostModelViewset, self).get_permissions()


# @api_view(['GET'])
# def recent_post_filter(request, slug):
#     category = Category.objects.get(slug=slug)
#     print(category)
#     post = Post.objects.filter(category_id=category.id)
#     print(post)
#     serializer = PostDetailSerializer(post, many=True)
#     return Response(serializer.data)

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'