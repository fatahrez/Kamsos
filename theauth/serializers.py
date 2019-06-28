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
        model = Pastoralist
        fields = '__all__'

    def create(self, validated_data):
        return Pastoralist.objects.create_pastoralist(**validated_data)

class AgrovetRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Agrovet
        fields = '__all__'

    def create(self, validated_data):
        return Agrovet.objects.create_agrovet(**validated_data)

class VetRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Vet
        fields = '__all__'

    def create(self, validated_data):
        return Vet.objects.create_vet(**validated_data)
