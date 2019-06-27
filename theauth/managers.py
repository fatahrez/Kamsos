from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

class PastoralistManager(BaseUserManager):
    def create_pastoralist(self, username, first_name, middle_name, last_name, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address')
        pastoralist = Pastoralist(username = username, first_name=first_name, last_name=last_name,
                        email=self.normalize_email(email),
                        animal=animal)
        pastoralist.set_password(password)
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
    def create_vet(self, username, first_name, middle_name, last_name, email, vet_hospital_name, password=None):
        if email is None:
            raise TypeError('Users must have an email address')
        vet = Vet(username=username, first_name=first_name, middle_name=middle_name, last_name=last_name,
            email=self.normalize_email(email),
            vet_hospital_name=vet_hospital_name)
        vet.set_password(password)
        vet.save()
        return vet
