from theauth.models import Vet
from rest_framework import serializers

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = ["id","first_name", "middle_name", "last_name", "username", "email"]
