import jwt
import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from .managers import (
    UserManager, PastoralistManager, AgrovetManager, VetManager
)




# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(db_index=True, max_length=254, unique=True)
    email = models.EmailField(db_index=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'middle_name', 'last_name']

    objects = UserManager()

    @property
    def token(self):
        dt = datetime.now() + timedelta(days=days)
        token = jwt.encode({
            'id': user_id,
            'exp': int(time.mktime(dt.timetuple()))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    def get_full_name(self):
        return (self.first_name+' '+self.last_name)

    def get_short_name(self):
        return self.first_name

    def natural_key(self):
        return (self.first_name, self.last_name)

    def __str__(self):
        return self.email

class Pastoralist(models.Model):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'middle_name','last_name']

    objects = PastoralistManager()

    def __str__(self):
        return self.username

class Agrovet(models.Model):

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['first_name', 'middle_name', 'last_name']

    objects=AgrovetManager()

    def __str__(self):
        return self.username

class Vet(models.Model):

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['first_name', 'middle_name', 'last_name']

    objects = VetManager()

    def __str__(self):
        return self.username
