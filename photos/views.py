from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def session_list(request):
    if (request.method == 'GET'):
        data = Session.objects.all()
        serializer = SessionSerializer(data, many=True)
        return Response(serializer.data)


class PhotoList(generics.ListAPIView):
    queryset = Photo.objects.all().order_by('-date_uploaded')
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'session', 'main_page']