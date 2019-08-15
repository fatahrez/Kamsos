from django.contrib import admin
from .models import Pastoralist, Vet, Agrovet, User

# Register your models here.
admin.site.register(Pastoralist)
admin.site.register(Vet)
admin.site.register(Agrovet)
admin.site.register(User)
