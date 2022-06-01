from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from posts.models import Post
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(ModelViewSet):
    """
    TODO: CREATE, UPDATE, PUT, PATCH, DELETE
    A viewset for viewing and editing user instances.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.root_nodes()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        else:
            return super(CommentViewSet, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(f"{instance.user}->{request.user}")
        if instance.user != request.user:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'messages': 'sorry invalid you...'
            })
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'messages': 'sorry invalid you...'
            })
        self.perform_destroy(instance)
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'messages': 'Deleted your comments sucessfully.'
        })

from django_filters.rest_framework import DjangoFilterBackend

class PostCommentList(ListAPIView):
    queryset = Comment.objects.root_nodes()
    serializer_class = CommentSerializer
    # lookup_field = 'post'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['post']
    def get_queryset(self):
        return Comment.objects.filter(post__slug='using-drf-effectively')

@api_view(['GET'])
def post_comments_list_api(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response({
            'messages': serializer.data,
            'status': status.HTTP_200_OK,
        })
    except Exception as e:
        print(e)
        return Response({
            'messages': 'Sorry not fount',
            'status': status.HTTP_404_NOT_FOUND,
        })