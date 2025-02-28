from rest_framework import serializers  
from .models import Detail, Folder, IMG, Hot_point, Count_details
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):  
    """Сериализатор для модели User"""  
  
    class Meta:  
        model = User  
        fields = ('id', 'username') 


class FolderSerializer(serializers.ModelSerializer):
    """Сериализатор для папок"""
    parent = FolderSerializer(read_only=True, many=True)

    class Meta:
        model = Folder
        fields = ('id', 'tag', 'VIN', 'description', 'parent')


class DetailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Деталь"""
    folder = FolderSerializer(read_only=True, many=True)

    class Meta:
        model = Detail
        fields = ('id', 'name', 'designation', 'assembly_disignation', 'note', 'link', 'folder')


class IMGSerializer(serializer.ModelSerializer):
    folder = FolderSerializer(read_only=True)
    
    class Meta:
        model = IMG
        fields = ('id',  'folder', 'path')


class Hot_pointSerializer(serializer.ModelSerializer):
    folder_link = FolderSerializer(read_only=True)
    IMG = IMGSerializer(read_only=True)

    class Meta:
        model = Hot_point
        fields = ('folder_link', 'coordinates', 'IMG', 'text')

class Count_detailsSerializer(serializer.ModelSerializer):
    folder = FolderSerializer(read_only=True)
    detail = DetailSerializer(read_only=True)

    class Meta:
        model = Count_details
        fields = ('folder', 'detail', 'count')