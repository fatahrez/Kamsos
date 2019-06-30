from django.conf.urls import url

from . import views

urlpatterns = [
    url('createpastoralist', views.PastoralistRegistration.as_view()),
    url('createagrovet', views.AgrovetRegistration.as_view()),
    url('createvet', views.VetRegistration.as_views()),
    url('login', views.UserLogin.as_view()),
]
