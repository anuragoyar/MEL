from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, get_user_model
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
import logging

from accounts.serializers import LoginSerializer, UserSerializer, UserRegistrationSerializer

# Set up logging
logger = logging.getLogger(__name__)

User = get_user_model()

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing tasks
    """
    permission_classes = [IsAuthenticated]

class SignupAPIView(APIView):
    """
    API endpoint for user registration
    """
    permission_classes = [AllowAny]  # Allow unauthenticated access
    serializer_class = UserRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Create the user
            user = serializer.save()
            
            # Log the registration
            logger.info(f"User registered successfully: {user.email}")
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            
            # Get user data for response
            user_serializer = UserSerializer(user)
            
            return Response({
                'success': True,
                'message': 'User registered successfully',
                'user': user_serializer.data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
            
        except IntegrityError as e:
            # This would catch duplicate email errors
            logger.warning(f"Registration failed due to integrity error: {str(e)}")
            return Response({
                'success': False,
                'error': 'A user with this email already exists.'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            # Catch any other exceptions
            logger.error(f"Registration failed due to unexpected error: {str(e)}")
            return Response({
                'success': False,
                'error': 'An unexpected error occurred during registration.'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginAPIView(APIView):
    """
    API endpoint for user authentication using JWT
    """
    permission_classes = [AllowAny]  # Allow unauthenticated access
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        remember_me = serializer.validated_data.get('remember_me', False)
        
        # Log login attempt (without password)
        logger.info(f"API login attempt for email: {email}")
        
        try:
            # Get the user by email
            user = User.objects.get(email=email)
            
            # Check if account is locked out
            if user.is_locked_out():
                logger.warning(f"Login attempt for locked account: {email}")
                return Response({
                    'success': False,
                    'error': 'Account is temporarily locked due to too many failed login attempts.'
                }, status=status.HTTP_401_UNAUTHORIZED)
                
            # Authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                # Login successful - reset failed attempts
                user.failed_login_attempts = 0
                user.lockout_until = None
                user.last_login = timezone.now()
                user.save(update_fields=['failed_login_attempts', 'lockout_until', 'last_login'])
                
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                
                # Set token expiry based on remember_me
                if remember_me:
                    # Extend token lifetime for "remember me" (14 days)
                    refresh.set_exp(lifetime=timezone.timedelta(days=14))
                
                # Get user data for response
                user_serializer = UserSerializer(user)
                
                logger.info(f"API login successful for email: {email}")
                return Response({
                    'success': True,
                    'user': user_serializer.data,
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                })
            else:
                # Login failed - increment failed attempts
                user.failed_login_attempts += 1
                
                # Lock account after 5 failed attempts
                if user.failed_login_attempts >= 5:
                    user.lockout_until = timezone.now() + timezone.timedelta(minutes=15)
                    logger.warning(f"Account locked for email: {email} after {user.failed_login_attempts} failed attempts")
                
                user.save(update_fields=['failed_login_attempts', 'lockout_until'])
                
                logger.warning(f"API login failed for email: {email} (Attempt {user.failed_login_attempts})")
                return Response({
                    'success': False,
                    'error': 'Invalid credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
                
        except User.DoesNotExist:
            # User not found - don't reveal this information
            logger.warning(f"API login attempt for non-existent email: {email}")
            return Response({
                'success': False,
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)


