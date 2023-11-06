from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework import viewsets

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