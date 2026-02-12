
from rest_framework.views import APIView
from rest_framework.parsers import  JSONParser
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from .models import Registration

# Create your views here.
class RegistrationListAPIView(APIView):
    """Handle registration API - List all or Create new"""
    parser_classes = [JSONParser]

    def get(self, request):
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)