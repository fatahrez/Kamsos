from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    is_pastoralist = models.BooleanField(default=False)
    is_agrovet = models.BooleanField(default=False)
    is_vet = models.BooleanField(default=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(request, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
