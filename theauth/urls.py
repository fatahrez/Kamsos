from django.conf.urls import url

from . import views

urlpatterns = [
    url('createpastoralist', views.PastoralistRegistration.as_view()),
    url('login', views.UserLogin.as_view()),
]
