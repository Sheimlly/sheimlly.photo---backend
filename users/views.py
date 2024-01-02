from .models import *
from .serializers import *
from rest_framework import viewsets, status, filters
from rest_framework.response import Response

# Create your views here.

class UserInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = UserInfo.objects.all().first()
        serializer = UserInfoSerializer(queryset, many=False)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = UserInfo.objects.get(pk=pk)
        serializer = UserInfoSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer