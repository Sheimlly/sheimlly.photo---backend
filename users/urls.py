from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'userinfo', UserInfoViewSet, basename='userinfo')
router.register(r'socialmedia', SocialMediaViewSet, basename='socialmedia')

urlpatterns = [
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    re_path(r'', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)