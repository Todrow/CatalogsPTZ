from rest_framework import serializers
from .models import Detail, Folder, IMG, Hot_point, Count_details


class DetailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Деталь"""

    class Meta:
        model = Detail
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    """Сериализатор для папок"""

    class Meta:
        model = Folder
        fields = '__all__'


class IMGSerializer(serializers.ModelSerializer):

    class Meta:
        model = IMG
        fields = '__all__'


class Hot_pointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hot_point
        fields = '__all__'


class Count_detailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Count_details
        fields = '_all__'
