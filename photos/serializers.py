from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'name', 'datetaken']

class PhotoSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    session_name = serializers.CharField(source='session.name', read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'session_name', 'image', 'category_name', 'category', 'date_created', 'date_uploaded']