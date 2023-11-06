from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'sessions', SessionViewSet, basename='sessions')
router.register(r'', PhotoViewSet, basename='photos')

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)