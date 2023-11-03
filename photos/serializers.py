from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'name_pl']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'name', 'name_pl', 'date_taken']

class PhotoSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True,)
    category_name_pl = serializers.CharField(source='category.name_pl', read_only=True)
    session_name = serializers.CharField(source='session.name', read_only=True)
    session_name_pl = serializers.CharField(source='session.name_pl', read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'name', 'session_name', 'session_name_pl', 'session', 'image', 'category_name', 'category_name_pl', 'category', 'date_created', 'date_uploaded', 'main_page']