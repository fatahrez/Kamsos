from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('createpastoralist', views.PastoralistRegistration.as_view()),
    url('createagrovet', views.AgrovetRegistration.as_view()),
    url('createvet', views.VetRegistration.as_view()),
    url('login', views.UserLogin.as_view()),
    url('user', views.UserRetrieveUpdateAPIView.as_view()),
    # url('password_reset/verify-token/', views.CustomPassword)
    url('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]
