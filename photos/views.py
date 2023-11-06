from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('-date_taken')
    serializer_class = SessionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-date_uploaded')
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'session', 'main_page']

    @action(detail=True, methods=['delete'])
    def delete_photo(self, request, pk=None):
        Photo.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        serializer = PhotoSerializer(Photo.objects.get(pk=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)