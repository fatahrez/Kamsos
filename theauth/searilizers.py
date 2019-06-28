from rest_framework import serializers

from .models import (
    Pastoralist, Agrovet, Vet
)


class PastoralistRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Pastoralist.objects.create_pastoralist(**validated_data)
