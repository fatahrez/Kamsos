from theauth.models import Vet
from rest_framework import viewsets
from .serializers import VetSerializer
from rest_framework import status, permissions


# Create your views here.
class CustomPermissionForPastoralist(permissions.BasePermission):

    def __init__(self, allowed_methods):
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if 'pastoralist_id' in request.session.keys:
            return request.method in self.allowed_methods


class VetViewSet(viewsets.ModelViewSet):
    queryset = Vet.objects.all()
    serializer_class = VetSerializer
