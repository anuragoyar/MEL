/**
 * Login Page JavaScript
 * Handles form validation, submission, and UI interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const loginForm = document.getElementById('login-form');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const emailError = document.getElementById('email-error');
    const passwordError = document.getElementById('password-error');
    const errorMessage = document.getElementById('error-message');
    const togglePasswordButton = document.getElementById('toggle-password');
    const rememberMeCheckbox = document.getElementById('remember-me');
    
    // Get the 'next' parameter from URL if present
    const urlParams = new URLSearchParams(window.location.search);
    const nextUrl = urlParams.get('next') || '/dashboard/';
    
    // Track page load for analytics
    trackEvent('Authentication', 'Login Page View');
    
    // Login attempts counter for rate limiting
    let loginAttempts = 0;
    const MAX_LOGIN_ATTEMPTS = 5;
    const LOCKOUT_TIME = 5 * 60 * 1000; // 5 minutes in milliseconds
    let lockoutEndTime = 0;
    
    // Email validation using regex
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    // Password validation (minimum 8 characters)
    function isValidPassword(password) {
        return password.length >= 8;
    }
    
    // Show error message
    function showError(element, message) {
        element.textContent = message;
        element.parentElement.querySelector('input').classList.add('error');
    }
    
    // Clear error message
    function clearError(element) {
        element.textContent = '';
        element.parentElement.querySelector('input').classList.remove('error');
    }
    
    // Show form error message
    function showFormError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.add('show');
        
        // Log error for analytics
        trackEvent('Authentication', 'Login Error', message);
    }
    
    // Clear form error message
    function clearFormError() {
        errorMessage.textContent = '';
        errorMessage.classList.remove('show');
    }
    
    // Validate email input
    function validateEmail() {
        const email = emailInput.value.trim();
        
        if (!email) {
            showError(emailError, 'Email is required');
            return false;
        } else if (!isValidEmail(email)) {
            showError(emailError, 'Please enter a valid email address');
            return false;
        } else {
            clearError(emailError);
            return true;
        }
    }
    
    // Validate password input
    function validatePassword() {
        const password = passwordInput.value;
        
        if (!password) {
            showError(passwordError, 'Password is required');
            return false;
        } else if (!isValidPassword(password)) {
            showError(passwordError, 'Password must be at least 8 characters');
            return false;
        } else {
            clearError(passwordError);
            return true;
        }
    }
    
    // Check if user is locked out due to too many login attempts
    function isLockedOut() {
        if (Date.now() < lockoutEndTime) {
            const remainingSeconds = Math.ceil((lockoutEndTime - Date.now()) / 1000);
            showFormError(`Too many login attempts. Please try again in ${remainingSeconds} seconds.`);
            return true;
        }
        return false;
    }
    
    // Handle form submission
    async function handleSubmit(event) {
        event.preventDefault();
        
        // Clear previous errors
        clearFormError();
        
        // Check for lockout
        if (isLockedOut()) {
            return;
        }
        
        // Validate form
        const isEmailValid = validateEmail();
        const isPasswordValid = validatePassword();
        
        if (!isEmailValid || !isPasswordValid) {
            return;
        }
        
        // Increment login attempts
        loginAttempts++;
        
        // Check if max attempts reached
        if (loginAttempts >= MAX_LOGIN_ATTEMPTS) {
            lockoutEndTime = Date.now() + LOCKOUT_TIME;
            showFormError(`Too many login attempts. Please try again in 5 minutes.`);
            trackEvent('Authentication', 'Login Lockout', `Attempts: ${loginAttempts}`);
            return;
        }
        
        // Get form data
        const email = emailInput.value.trim();
        const password = passwordInput.value;
        const rememberMe = rememberMeCheckbox.checked;
        
        // Track login attempt
        trackEvent('Authentication', 'Login Attempt', `Email: ${email.substring(0, 3)}...`);
        
        try {
            // Submit form data to server
            const response = await fetch('', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    email,
                    password,
                    remember_me: rememberMe
                })
            });
            
            const data = await response.json();
            
            if (response.ok && data.success) {
                // Track successful login
                trackEvent('Authentication', 'Login Success');
                
                // Reset login attempts on success
                loginAttempts = 0;
                
                // Redirect to dashboard or specified URL
                window.location.href = data.redirect || nextUrl;
            } else {
                // Handle error response
                if (response.status === 401) {
                    showFormError('Invalid email or password. Please try again.');
                    trackEvent('Authentication', 'Login Failure', 'Invalid Credentials');
                } else if (response.status === 429) {
                    // Rate limiting from server
                    showFormError('Too many login attempts. Please try again later.');
                    trackEvent('Authentication', 'Login Rate Limited');
                } else {
                    showFormError(data.error || 'An error occurred. Please try again later.');
                    trackEvent('Authentication', 'Login Error', `Status: ${response.status}`);
                }
            }
        } catch (error) {
            console.error('Login error:', error);
            showFormError('An unexpected error occurred. Please try again.');
            trackEvent('Authentication', 'Login Error', 'Network Error');
        }
    }
    
    // Toggle password visibility
    function togglePasswordVisibility() {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        
        // Toggle show/hide text
        document.querySelector('.show-password-icon').style.display = 
            type === 'password' ? 'inline' : 'none';
        document.querySelector('.hide-password-icon').style.display = 
            type === 'password' ? 'none' : 'inline';
        
        // Track for analytics
        trackEvent('Authentication', 'Toggle Password Visibility', type);
    }
    
    // Event Listeners
    loginForm.addEventListener('submit', handleSubmit);
    
    // Real-time validation
    emailInput.addEventListener('blur', validateEmail);
    passwordInput.addEventListener('blur', validatePassword);
    
    // Clear errors when user starts typing
    emailInput.addEventListener('input', () => clearError(emailError));
    passwordInput.addEventListener('input', () => clearError(passwordError));
    
    // Toggle password visibility
    togglePasswordButton.addEventListener('click', togglePasswordVisibility);
    
    // Accessibility - allow Enter key on toggle password button
    togglePasswordButton.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            togglePasswordVisibility();
        }
    });
}); 