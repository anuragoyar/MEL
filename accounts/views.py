from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import JsonResponse
import json
import logging
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import re

# Set up logging
logger = logging.getLogger(__name__)

User = get_user_model()

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
            
            # Get the next URL from the request
            next_url = request.GET.get('next', '/dashboard/')
            
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
                return JsonResponse({'success': True, 'redirect': next_url})
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
    if request.method == 'POST':
        try:
            # Get registration data from request
            data = json.loads(request.body)
            
            # Forward the request to the API
            api_url = request.build_absolute_uri('/api/v1/auth/signup')
            
            # Make the API request
            response = requests.post(
                api_url,
                json=data,
                headers={'Content-Type': 'application/json'}
            )
            
            # Return the API response
            return JsonResponse(response.json(), status=response.status_code)
                
        except json.JSONDecodeError:
            logger.error("Invalid JSON in signup request")
            return JsonResponse({'success': False, 'error': 'Invalid request format'}, status=400)
        except Exception as e:
            logger.error(f"Signup error: {str(e)}")
            return JsonResponse({'success': False, 'error': 'An error occurred during signup'}, status=500)
    
    # GET request - render signup page
    return render(request, 'accounts/signup.html')

@login_required
def dashboard(request):
    """
    View for rendering the dashboard after successful login.
    This view is protected and requires authentication.
    """
    context = {
        'user': request.user,
        'page_title': 'Dashboard',
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def logout_view(request):
    """
    View for handling user logout.
    """
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('accounts:login')
    return redirect('accounts:dashboard')

@login_required
def profile(request):
    """
    View for displaying and updating user profile information.
    This view is protected and requires authentication.
    """
    if request.method == 'POST':
        try:
            # Get form data
            full_name = request.POST.get('full_name', '').strip()
            email = request.POST.get('email', '').strip()

            # Validate full name
            if not full_name:
                return JsonResponse({'success': False, 'error': 'Full name is required'}, status=400)
            if len(full_name.split()) < 2:
                return JsonResponse({'success': False, 'error': 'Please provide both first and last name'}, status=400)

            # Validate email
            if not email:
                return JsonResponse({'success': False, 'error': 'Email is required'}, status=400)
            if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
                return JsonResponse({'success': False, 'error': 'Please provide a valid email address'}, status=400)

            # Check if email is already taken by another user
            if User.objects.exclude(id=request.user.id).filter(email=email).exists():
                return JsonResponse({'success': False, 'error': 'This email is already in use'}, status=400)

            # Split full name into first and last name
            name_parts = full_name.split(maxsplit=1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''

            # Update user profile
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            return JsonResponse({
                'success': True,
                'message': 'Profile updated successfully',
                'data': {
                    'full_name': user.get_full_name(),
                    'email': user.email
                }
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'An error occurred while updating profile'}, status=500)

    context = {
        'user': request.user,
        'page_title': 'Profile',
        'date_joined': request.user.date_joined.strftime('%B %d, %Y')
    }
    return render(request, 'accounts/profile.html', context) 