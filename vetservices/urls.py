from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.VetViewSet)
# router.register(r'requestvet', views.RequestVet.as_view())

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'requestvet', views.RequestVet.as_view(), name='request-vet')
]
