from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FavoriteSerializer
from .models import Favorite


class FavoriteModelViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
