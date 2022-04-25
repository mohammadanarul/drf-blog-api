from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostModelViewset(ModelViewSet):
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET'])
def recent_post_filter(request, category):
    recent_post = Post.objects.filter(category__slug=category)
    serializer = PostDetailSerializer(recent_post, many=True)
    return Response(serializer.data)
# class PostModelViewset(ModelViewSet):
#     lookup_field = 'slug'
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
