from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post
from likes.models import Like
from likes.serializers import LikeSerializer


class PostDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    category = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    post_like = serializers.SerializerMethodField()
    # post_like = LikeSerializer(many=True)
    # status = serializers.ChoiceField(allow_blank=True)

    def get_category(self, obj):

        # Use a try - except block if needed

        return obj.category.name

    def get_user(self, obj):

        # Use a try - except block if needed

        return obj.user.username

    def get_post_like(self, obj):
        # post like counter
        try:
            obj_like = Like.objects.get(post_id=obj.id)
            return obj_like.liked.all().count()
        except Exception as e:
            print(e)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'slug', 'description',
                  'category', 'tags', 'post_like', 'status']


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'
