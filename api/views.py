from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
import logging

# Set up logging
logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing tasks
    """
    permission_classes = [IsAuthenticated]

class LoginAPIView(APIView):
    """
    API endpoint for user authentication
    """
    permission_classes = []  # Allow unauthenticated access
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        remember_me = request.data.get('remember_me', False)
        
        # Log login attempt (without password)
        logger.info(f"API login attempt for email: {email}")
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Login successful
            login(request, user)
            
            # Set session expiry based on remember_me
            if remember_me:
                # Session will last for 2 weeks
                request.session.set_expiry(1209600)
            else:
                # Session will end when browser is closed
                request.session.set_expiry(0)
            
            logger.info(f"API login successful for email: {email}")
            return Response({
                'success': True,
                'redirect': '/dashboard/',
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'name': user.get_full_name()
                }
            })
        else:
            # Login failed
            logger.warning(f"API login failed for email: {email}")
            return Response({
                'success': False,
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)


