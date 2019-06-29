from django.contrib.auth import authenticate

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

class UserLoginSearilizer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with email and password is required to login'
            )

        try:
            user_obj = Pastoralist.objects.get(email=user.email)
        except Pastoralist.DoesNotExist:
            user_obj = None

        try:
            if user_obj is None:
                user_obj = Agrovet.objects.get(email=user.email)
        except Agrovet.DoesNotExist:
            raise serializers.ValidationError(
                'User with this email and password does not exist'
            )

        try:
            if user_obj is None:
                user_obj = Vet.objects.get(email=user.email)
        except Vet.DoesNotExist:
            raise serializers.ValidationError(
                'User with this email and password does not exist'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )

        return{
            'email': user.email,
            'token': user.token
        }
