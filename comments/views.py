from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(ModelViewSet):
    """
    TODO: CREATE, UPDATE, PUT, PATCH, DELETE
    A viewset for viewing and editing user instances.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        elif self.action == 'retrieve':
            return [IsAuthenticated()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'update':
            return [IsAuthenticated()]
        elif self.action == 'partial_update':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsAuthenticated()]
        else:
            return super(self, CommentViewSet).get_permissions()

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
