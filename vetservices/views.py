from theauth.models import Vet
from rest_framework import viewsets
from .serializers import VetSerializer

# Create your views here.
class VetViewSet(viewsets.ModelViewSet):
    queryset = Vet.objects.all()
    serializer_class = VetSerializer
