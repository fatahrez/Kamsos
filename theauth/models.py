import jwt
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.contrib.auth.models import BaseUserManager

# from .managers import (
#     UserManager, PastoralistManager, AgrovetManager, VetManager
# )

# Create your models here.
class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

class PastoralistManager(BaseUserManager):
    def create_pastoralist(self, username, first_name, middle_name, last_name, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address')
        pastoralist = Pastoralist(username = username, first_name=first_name,middle_name=middle_name, last_name=last_name,
                        email=self.normalize_email(email))
        pastoralist.set_password(password)
        pastoralist.save()
        return pastoralist

class AgrovetManager(BaseUserManager):
    def create_agrovet(self, username, first_name, middle_name, last_name, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        agrovet = Agrovet(username = username, first_name=first_name, middle_name=middle_name, last_name=last_name,
                    email=self.normalize_email(email))
        agrovet.set_password(password)
        agrovet.save()
        return agrovet

class VetManager(BaseUserManager):
    def create_vet(self, username, first_name, middle_name, last_name, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address')
        vet = Vet(username=username, first_name=first_name, middle_name=middle_name, last_name=last_name,
            email=self.normalize_email(email))
        vet.set_password(password)
        vet.save()
        return vet

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(db_index=True, max_length=254, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'middle_name', 'last_name']

    objects = UserManager()

    @property
    def token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    def get_full_name(self):
        return (self.first_name+' '+self.last_name)

    def get_short_name(self):
        return self.first_name

    def natural_key(self):
        return (self.first_name, self.last_name)

    def __str__(self):
        return self.username

class Pastoralist(User, PermissionsMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'middle_name','last_name']

    objects = PastoralistManager()

    def __str__(self):
        return self.username

class Agrovet(User, PermissionsMixin):

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['first_name', 'middle_name', 'last_name']

    objects=AgrovetManager()

    def __str__(self):
        return self.username

class Vet(User, PermissionsMixin):

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['first_name', 'middle_name', 'last_name']

    objects = VetManager()

    def __str__(self):
        return self.username
