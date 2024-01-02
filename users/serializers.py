from rest_framework import serializers
from .models import *

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'email', 'phone_number']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'name', 'username', 'link']