from django.db import models

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage

from django.conf import settings 

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

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("http://localhost:3000/login/reset-password/"), reset_password_token.key)
    
    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password Reset for {title}".format(title=settings.SITE_NAME),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )