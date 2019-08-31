from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from theauth.models import Vet
from vetservices.renderer import VetJSONRenderer
from .serializers import VetSerializer, RequestVetSerializer
from rest_framework import status, permissions, generics, mixins


# Create your views here.
class VetViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    lookup_field = 'slug'
    queryset = Vet.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (VetJSONRenderer,)
    serializer_class = VetSerializer

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def create(self, request):
        serializer_context = {
            'request': request
        }
        serializer_data = request.data.get('vet', {})

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(page, context=serializer_context, many=True)

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, slug):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Vet.DoesNotExist:
            raise NotFound('This vet is not found')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

class RequestVet(APIView):
    serializer_class = RequestVetSerializer
    # authentication_classes = TokenAuthentication
    # permission_classes = (partial(CustomPermissionForPastoralist, ['GET', 'HEAD', 'POST']), permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAuthenticated,)

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
