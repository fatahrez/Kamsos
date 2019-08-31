import uuid
from django.db import models

from profiles.models import Profile
from theauth.models import Pastoralist, Vet


# Create your models here.
class OrderVet(models.Model):
    pastoralist_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    vet_id = models.ForeignKey(Vet, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
