from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import (
    User, Pastoralist, Agrovet, Vet
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
        fields = ["email", "username", "token", "password"]

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
        fields = ["email", "username", "token", "password"]

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
        fields = ["email", "username", "token", "password"]

    def create(self, validated_data):
        return Vet.objects.create_vet(**validated_data)


class UserLoginSearilizer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'password is required to login'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with email and password is required to login'
            )

        try:
            userObj = User.objects.get(email=user.email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )

        # try:
        #     if userObj is None:
        #         userObj = Agrovet.objects.get(email=user.email)
        # except Agrovet.DoesNotExist:
        #     raise serializers.ValidationError(
        #         'User with given email and password does not exists'
        #     )
        #
        # try:
        #     if userObj is None:
        #         userObj = Vet.objects.get(email=user.email)
        # except Vet.DoesNotExist:
        #     raise serializers.ValidationError(
        #         'User with given email and password does not exists'
        #     )
        # try:
        #     userObj = Vet.objects.get(email=user.email)
        # except Vet.DoesNotExist:
        #     raise serializers.ValidationError(
        #         'User with given email and password does not exists'
        #     )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )

        return {
            'email': user.email,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password'
        )

        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_passsword(password)
        instance.save()

        return instance