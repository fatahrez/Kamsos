from django.config.urls import urls
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'vets', views.VetViewSet)

urlpatterns =[
    url(r'', include(router.urls))
]
