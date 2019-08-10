from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView

from theauth.models import Vet
from rest_framework import viewsets
from .serializers import VetSerializer, RequestVetSerializer
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


class RequestVet(APIView):
    serializer_class = RequestVetSerializer
    permission_classes = (partial(CustomPermissionForPastoralist, ['GET', 'HEAD', 'POST']),)

    def post(self, request, format=None):
        context = {
            'pastoralist_id': request.session['pastoralist_id'],
            'vet_id': request.session['vet_id']
        }
        serializer = RequestVetSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            data = {
                "success": "You have set an appointment successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)