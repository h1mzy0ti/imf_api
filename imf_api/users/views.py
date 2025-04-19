from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__) 

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = [JSONParser]

    def post(self, request):
        
        logger.info(f"POST Request Data: {request.data}")  # Log the request data
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            logger.info(f"Serializer is valid: {serializer.validated_data}")
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "message": "User created successfully!",
                "access_token": access_token,
                "refresh_token": str(refresh)
            }, status=status.HTTP_201_CREATED)

        logger.error(f"Serializer errors: {serializer.errors}")  # Log errors if serializer is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class LoginView(TokenObtainPairView):
    pass

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
