from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Like
from .serializers import LikeSerializer
from rest_framework.response import Response
from accounts.models import Account
from posts.models import Post
from django.db.models import Q
from rest_framework import authentication, permissions, status


class LikeModelViewset(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'messages': 'Your liked models delete sucessfully.'
        })


class LikeView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug, format=None):
        user = request.user
        print(user)
        post = Post.objects.get(slug=slug)
        account = Account.objects.get(id=user.id)
        likes, created = Like.objects.get_or_create(
            post=post,
        )
        print(user.id)
        if Like.objects.filter(post=post, liked=account).exists():
            likes.liked.remove(account)
            # likes.save()
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Alredy unliked post 😢"
            })
        likes.liked.add(account)
        likes.save()
        print('successfully liked you in post.')
        return Response({
            "status": status.HTTP_200_OK,
            "message": "successfully liked you in post ❤️"
        })
