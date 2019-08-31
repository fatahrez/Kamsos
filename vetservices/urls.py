from django.conf.urls import url, include
from rest_framework import routers

from theauth.models import Vet
from vetservices.serializers import VetSerializer
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'vets', views.VetViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'vets/(?P<vet_slug>[-\w]+)/request/?$', views.RequestVetCreateAPIView.as_view(), name='request-vet')
]
