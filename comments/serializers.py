from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    children = RecursiveField(many=True, required=False)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'parent', 'children', 'publish']
        # depth = 1
