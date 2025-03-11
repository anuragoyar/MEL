from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
import logging

# Set up logging
logger = logging.getLogger(__name__)

def login_view(request):
    """
    View for handling user login.
    """
    if request.method == 'POST':
        try:
            # Get credentials from request
            data = json.loads(request.body)
            email = data.get('email', '')
            password = data.get('password', '')
            remember_me = data.get('remember_me', False)
            
            # Log login attempt (without password)
            logger.info(f"Login attempt for email: {email}")
            
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
                
                logger.info(f"Login successful for email: {email}")
                return JsonResponse({'success': True, 'redirect': '/dashboard/'})
            else:
                # Login failed
                logger.warning(f"Login failed for email: {email}")
                return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
                
        except json.JSONDecodeError:
            logger.error("Invalid JSON in login request")
            return JsonResponse({'success': False, 'error': 'Invalid request format'}, status=400)
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            return JsonResponse({'success': False, 'error': 'An error occurred during login'}, status=500)
    
    # GET request - render login page
    return render(request, 'accounts/login.html')

def forgot_password(request):
    """
    View for handling forgot password requests.
    """
    return render(request, 'accounts/forgot_password.html')

def signup(request):
    """
    View for handling user registration.
    """
    return render(request, 'accounts/signup.html') 