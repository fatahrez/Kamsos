from rest_framework.exceptions import ValidationError

from profiles.serializers import ProfileSerializer
from theauth.models import Vet, Pastoralist
from rest_framework import serializers

from vetservices.models import OrderVet


class VetSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Vet
        fields = ["id", "first_name", "middle_name", "slug", "last_name", "username", "email", "telephone_number",
                  "county",
                  "sub_county", "qualifications", "vet_image"]

    def create(self, validated_data):
        vet = Vet.objects.create(**validated_data)

        return vet

    def get_created_at(self, instance):
        return instance.created_at.isoformat()


class RequestVetSerializer(serializers.ModelSerializer):
    pastoralist_id = ProfileSerializer(required=False)

    createdAt = serializers.SerializerMethodField(method_name='get_created_at')

    vet_id = VetSerializer()

    class Meta:
        model = OrderVet
        fields = (
            'pastoralist_id', 'vet_id', 'createdAt',
        )

    def create(self, validated_data):
        pastoralist_id = self.context['pastoralist_id']
        vet_id = self.context['vet_id']

    def get_created_at(self, instance):
        return instance.created_at.isoformat
