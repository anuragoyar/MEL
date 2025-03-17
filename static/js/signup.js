/**
 * Signup Page JavaScript
 * Handles form validation, submission, and UI interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const signupForm = document.getElementById('signup-form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirm-password');
    const nameError = document.getElementById('name-error');
    const emailError = document.getElementById('email-error');
    const passwordError = document.getElementById('password-error');
    const confirmPasswordError = document.getElementById('confirm-password-error');
    const errorMessage = document.getElementById('error-message');
    const togglePasswordButton = document.getElementById('toggle-password');
    const toggleConfirmPasswordButton = document.getElementById('toggle-confirm-password');
    
    // Track page load for analytics
    if (typeof trackEvent === 'function') {
        trackEvent('Authentication', 'Signup Page View');
    }
    
    // Email validation using regex
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    // Password validation
    function isValidPassword(password) {
        // At least 8 characters
        if (password.length < 8) {
            return { valid: false, message: 'Password must be at least 8 characters long.' };
        }
        
        // At least one digit
        if (!/\d/.test(password)) {
            return { valid: false, message: 'Password must contain at least one digit.' };
        }
        
        // At least one special character
        if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
            return { valid: false, message: 'Password must contain at least one special character.' };
        }
        
        return { valid: true };
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
        if (typeof trackEvent === 'function') {
            trackEvent('Authentication', 'Signup Error', message);
        }
    }
    
    // Clear form error message
    function clearFormError() {
        errorMessage.textContent = '';
        errorMessage.classList.remove('show');
    }
    
    // Validate name
    function validateName() {
        const name = nameInput.value.trim();
        
        if (name === '') {
            showError(nameError, 'Please enter your name.');
            return false;
        }
        
        // Split name into first and last name
        const nameParts = name.split(' ');
        if (nameParts.length < 2) {
            showError(nameError, 'Please enter your full name (first and last name).');
            return false;
        }
        
        clearError(nameError);
        return true;
    }
    
    // Validate email
    function validateEmail() {
        const email = emailInput.value.trim();
        
        if (email === '') {
            showError(emailError, 'Please enter your email address.');
            return false;
        }
        
        if (!isValidEmail(email)) {
            showError(emailError, 'Please enter a valid email address.');
            return false;
        }
        
        clearError(emailError);
        return true;
    }
    
    // Validate password
    function validatePassword() {
        const password = passwordInput.value;
        
        if (password === '') {
            showError(passwordError, 'Please enter a password.');
            return false;
        }
        
        const validation = isValidPassword(password);
        if (!validation.valid) {
            showError(passwordError, validation.message);
            return false;
        }
        
        clearError(passwordError);
        return true;
    }
    
    // Validate confirm password
    function validateConfirmPassword() {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
        
        if (confirmPassword === '') {
            showError(confirmPasswordError, 'Please confirm your password.');
            return false;
        }
        
        if (password !== confirmPassword) {
            showError(confirmPasswordError, 'Passwords do not match.');
            return false;
        }
        
        clearError(confirmPasswordError);
        return true;
    }
    
    // Toggle password visibility
    function togglePasswordVisibility(inputElement, button) {
        const type = inputElement.getAttribute('type') === 'password' ? 'text' : 'password';
        inputElement.setAttribute('type', type);
        
        // Toggle show/hide icons
        button.querySelector('.show-password-icon').style.display = 
            type === 'password' ? 'inline' : 'none';
        button.querySelector('.hide-password-icon').style.display = 
            type === 'password' ? 'none' : 'inline';
    }
    
    // Handle form submission
    async function handleSubmit(event) {
        event.preventDefault();
        
        // Clear any previous errors
        clearFormError();
        
        // Validate all fields
        const isNameValid = validateName();
        const isEmailValid = validateEmail();
        const isPasswordValid = validatePassword();
        const isConfirmPasswordValid = validateConfirmPassword();
        
        // If any validation fails, stop submission
        if (!isNameValid || !isEmailValid || !isPasswordValid || !isConfirmPasswordValid) {
            return;
        }
        
        // Get form data
        const fullName = nameInput.value.trim();
        const nameParts = fullName.split(' ');
        const firstName = nameParts[0];
        const lastName = nameParts.slice(1).join(' ');
        
        const formData = {
            email: emailInput.value.trim(),
            first_name: firstName,
            last_name: lastName,
            password: passwordInput.value,
            password_confirm: confirmPasswordInput.value
        };
        
        try {
            // Show loading state
            const submitButton = signupForm.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.textContent;
            submitButton.textContent = 'Creating Account...';
            submitButton.disabled = true;
            
            // Send API request
            const response = await fetch('/api/v1/auth/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            // Reset button state
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
            
            if (response.ok) {
                // Signup successful
                if (typeof trackEvent === 'function') {
                    trackEvent('Authentication', 'Signup Success');
                }
                
                // Store tokens in localStorage
                if (data.tokens) {
                    localStorage.setItem('access_token', data.tokens.access);
                    localStorage.setItem('refresh_token', data.tokens.refresh);
                }
                
                // Redirect to dashboard or show success message
                window.location.href = '/dashboard/';
            } else {
                // Signup failed
                if (data.email) {
                    showError(emailError, data.email[0]);
                } else if (data.password) {
                    showError(passwordError, data.password[0]);
                } else if (data.password_confirm) {
                    showError(confirmPasswordError, data.password_confirm[0]);
                } else if (data.error) {
                    showFormError(data.error);
                } else {
                    showFormError('An error occurred during signup. Please try again.');
                }
                
                if (typeof trackEvent === 'function') {
                    trackEvent('Authentication', 'Signup Error', data.error || 'Unknown error');
                }
            }
        } catch (error) {
            console.error('Signup error:', error);
            showFormError('An unexpected error occurred. Please try again later.');
            
            if (typeof trackEvent === 'function') {
                trackEvent('Authentication', 'Signup Error', error.message);
            }
        }
    }
    
    // Event Listeners
    signupForm.addEventListener('submit', handleSubmit);
    
    // Toggle password visibility
    togglePasswordButton.addEventListener('click', () => togglePasswordVisibility(passwordInput, togglePasswordButton));
    toggleConfirmPasswordButton.addEventListener('click', () => togglePasswordVisibility(confirmPasswordInput, toggleConfirmPasswordButton));
    
    // Accessibility - allow Enter key on toggle password buttons
    togglePasswordButton.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            togglePasswordVisibility(passwordInput, togglePasswordButton);
        }
    });
    
    toggleConfirmPasswordButton.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            togglePasswordVisibility(confirmPasswordInput, toggleConfirmPasswordButton);
        }
    });
    
    // Real-time validation
    nameInput.addEventListener('blur', validateName);
    emailInput.addEventListener('blur', validateEmail);
    passwordInput.addEventListener('blur', validatePassword);
    confirmPasswordInput.addEventListener('blur', validateConfirmPassword);
    
    // Clear errors when user starts typing
    nameInput.addEventListener('input', () => clearError(nameError));
    emailInput.addEventListener('input', () => clearError(emailError));
    passwordInput.addEventListener('input', () => clearError(passwordError));
    confirmPasswordInput.addEventListener('input', () => clearError(confirmPasswordError));
}); 