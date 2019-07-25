from theauth.models import Vet
from rest_framework import serializers

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = '__all__'
    
