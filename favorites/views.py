from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FavoriteSerializer
from .models import Favorite


class FavoriteModelViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializers_class = FavoriteSerializer
