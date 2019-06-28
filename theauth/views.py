from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class PastoralistRegistration(APIView):
    permission_classes = (AllowAny,)
    
