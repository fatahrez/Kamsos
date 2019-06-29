# from django.contrib.auth.models import BaseUserManager
#
# from django.db import models
# from .models import (
#     User, Pastoralist, Agrovet, Vet
# )

# class UserManager(BaseUserManager):
#     def get_by_natural_key(self, email):
#         return self.get(email=email)
#
# class PastoralistManager(BaseUserManager):
#     def create_pastoralist(self, username, first_name, middle_name, last_name, email, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address')
#         pastoralist = self.model(username = username, first_name=first_name,middle_name=middle_name, last_name=last_name,
#                         email=self.normalize_email(email))
#         pastoralist.set_password(password)
#         return pastoralist
#
# class AgrovetManager(BaseUserManager):
#     def create_agrovet(self, username, first_name, middle_name, last_name, email, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address.')
#         agrovet = Agrovet(username = username, first_name=first_name, middle_name=middle_name, last_name=last_name,
#                     email=self.normalize_email(email))
#         agrovet.set_password(password)
#         agrovet.save()
#         return agrovet
#
# class VetManager(BaseUserManager):
#     def create_vet(self, username, first_name, middle_name, last_name, email, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address')
#         vet = Vet(username=username, first_name=first_name, middle_name=middle_name, last_name=last_name,
#             email=self.normalize_email(email))
#         vet.set_password(password)
#         vet.save()
#         return vet
