from rest_framework import serializers
from .models import Detail, Folder, IMG, Hot_point, Count_details


class DetailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Деталь"""

    class Meta:
        model = Detail
        fields = '__all__'


class FolderCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания папок"""
    IMG = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='path')
    childs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Folder
        depth = 0
        fields = ['id', 'tag', 'VIN', 'description', 'parent', 'IMG', 'childs']


class FolderReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения папок"""
    IMG = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='path')

    class Meta:
        model = Folder
        depth = 1
        fields = ['id', 'tag', 'VIN', 'description', 'parent', 'IMG', 'childs']


class IMGSerializer(serializers.ModelSerializer):
    hot_points = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = IMG
        fields = ['id', 'folder', 'path', 'hot_points']


class Hot_pointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hot_point
        fields = '__all__'


class Count_detailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Count_details
        fields = '_all__'
