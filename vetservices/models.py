import uuid
from django.db import models
from theauth.models import Pastoralist, Vet


# Create your models here.
class OrderVet(models.Model):
    pastoralist_id = models.ForeignKey(Pastoralist, on_delete=models.CASCADE)
    vet_id = models.ForeignKey(Vet, on_delete=models.CASCADE)
    booked_time = models.DateTimeField(auto_now_add=True)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)