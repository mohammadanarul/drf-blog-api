from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    liked = serializers.StringRelatedField(many=True)

    class Meta:
        model = Like
        fields = ['id', 'post', 'liked']
