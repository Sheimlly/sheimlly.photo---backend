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

def path_file_name(instance, filename):
    print(instance.name)
    ext = filename.split('.')[-1]
    return '/'.join(['media', 'Socials', '{}.{}'.format(instance.name, ext)])

class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    icon = models.ImageField(upload_to=path_file_name)
    username = models.CharField(max_length=50, blank=False)
    link = models.CharField(max_length=100, blank=False)

    def save(self, *args, **kwargs):
        super(SocialMedia, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

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

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("http://localhost:5173/password_reset/"), reset_password_token.key)
    
    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password Reset for {title}".format(title="portfolio user account"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST,
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )