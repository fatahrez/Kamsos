from django.conf.urls import url

from . import views

urlpatterns = [
    url('login', views.ObtainAuthToken.as_view())
]
