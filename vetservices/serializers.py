from rest_framework.exceptions import ValidationError

from theauth.models import Vet, Pastoralist
from rest_framework import serializers

from vetservices.models import OrderVet


class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = ["id", "first_name", "middle_name", "last_name", "username", "email", "telephone_number", "county",
                  "sub_county", "qualifications", "vet_image"]


class RequestVetSerializer(serializers.Serializer):
    vet_id = serializers.CharField()

    def validate(self, data):
        vet_id = data.get("vet_id")

        if not vet_id:
            raise ValidationError("Vet does not exist")
        try:
            vet = Vet.objects.get(pk=vet_id)
        except Vet.DoesNotExist:
            raise ValidationError("Vet doesn't exist")

        return data

    def create(self, validated_data):
        vet_id = validated_data.pop('vet_id')
        pastoralist_id = self.context.get("pastoralist_id")
        pastoralist = Pastoralist.objects.get(pk=pastoralist_id)
        vet = Vet.objects.get(pk=vet_id)
        obj1 = OrderVet()
        obj1.pastoralist_id = pastoralist
        obj1.vet_id = vet
        obj1.save()
        return obj1