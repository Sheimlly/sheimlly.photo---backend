from django.contrib import admin
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    re_path(r'^photos/$', PhotoList.as_view()),
    # re_path(r'^photos/re_path', photo_list_2),
    path('categories/', category_list),
    path('sessions/', session_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)