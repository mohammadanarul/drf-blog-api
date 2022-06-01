from rest_framework import serializers
from posts.serializers import PostSerializerId
from accounts.serializers import AccountSerializerId
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    # user = AccountSerializerId
    # post = PostSerializerId()
    class Meta:
        model = Favorite
        fields = '__all__'
