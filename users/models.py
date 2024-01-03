from django.db import models

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage

from django.conf import settings 

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager

# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, blank=False)
    phone_number = models.IntegerField(blank=True)

class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    link = models.CharField(max_length=100, blank=False)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin