from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from .views import *
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'userinfo', UserInfoViewSet, basename='userinfo')
router.register(r'socialmedia', SocialMediaViewSet, basename='socialmedia')

app_name = 'users'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    re_path(r'', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)