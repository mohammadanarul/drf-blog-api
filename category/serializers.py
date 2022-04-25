from rest_framework import serializers
from .models import Category
from rest_framework_recursive.fields import RecursiveField


class CategorySerializer(serializers.ModelSerializer):
    # children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']


class CategoryParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class CategoryModelSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'children', 'slug']
