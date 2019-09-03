from rest_framework.exceptions import NotFound, ParseError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from theauth.models import Vet
from vetservices.models import OrderVet
from vetservices.renderer import VetJSONRenderer, RequestJSONRenderer
from .serializers import VetSerializer, RequestVetSerializer
from rest_framework import status, permissions, generics, mixins


# Create your views here.
class VetViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet):
    lookup_field = 'slug'
    queryset = Vet.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (VetJSONRenderer,)
    serializer_class = VetSerializer

    def get_queryset(self):
        queryset = Vet.objects.all()

        return queryset

    @classmethod
    def get_extra_actions(cls):
        return []

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


class RequestVetCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'vet__slug'
    lookup_url_kwarg = 'vet_slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = OrderVet.objects.all()
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = RequestVetSerializer

    def create(self, request, vet_slug=None):
        data = request.data.get('vet_request', {})
        context = {'pastoralist_id': request.user.profile}

        try:
            context['vet'] = Vet.objects.get(slug=vet_slug)
        except Vet.DoesNotExist:
            raise NotFound('The vet you have chosen is not available')

        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
