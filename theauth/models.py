import jwt
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('User must have email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
      """
      Create and return a `User` with superuser powers.
      Superuser powers means that this use is an admin that can do anything
      they want.
      """
      if password is None:
          raise TypeError('Superusers must have a password.')

      user = self.create_user(username, email, password)
      user.is_superuser = True
      user.is_staff = True
      user.save()

      return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class PastoralistManager(BaseUserManager):
    def create_pastoralist(self, username, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address')
        pastoralist = Pastoralist(username=username, email=self.normalize_email(email))
        pastoralist.set_password(password)
        pastoralist.save()
        return pastoralist


class AgrovetManager(BaseUserManager):
    def create_agrovet(self, username, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        agrovet = Agrovet(username=username, email=self.normalize_email(email))
        agrovet.set_password(password)
        agrovet.save()
        return agrovet


class VetManager(BaseUserManager):
    def create_vet(self, username, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address')
        vet = Vet(username=username, email=self.normalize_email(email))
        vet.set_password(password)
        vet.save()
        return vet


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(db_index=True, max_length=254, unique=True, blank=True, null=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'username']

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
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def natural_key(self):
        return self.first_name, self.last_name

    def __str__(self):
        return self.username


class Pastoralist(User, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'username']

    objects = PastoralistManager()

    def __str__(self):
        return self.username


class Agrovet(User, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'username']

    objects = AgrovetManager()

    def __str__(self):
        return self.username


class Vet(User, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'username']

    objects = VetManager()

    slug = models.SlugField(db_index=True, max_length=255, unique=True, null=True)
    telephone_number = models.CharField(max_length=13, unique=True, null=True)
    county = models.CharField(max_length=30, null=True)
    sub_county = models.CharField(max_length=30, null=True)
    qualifications = models.TextField(null=True)
    vet_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username
