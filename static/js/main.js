/**
 * Main JavaScript File
 * Contains common functionality used across the site
 */

// CSRF Token handling for AJAX requests
function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

// Add CSRF token to all AJAX requests
document.addEventListener('DOMContentLoaded', function() {
    // Set up AJAX requests to include CSRF token
    const csrftoken = getCSRFToken();
    
    // Helper for making API requests
    window.apiRequest = async function(url, method = 'GET', data = null) {
        const options = {
            method: method,
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
            credentials: 'same-origin'
        };
        
        if (data && (method === 'POST' || method === 'PUT' || method === 'PATCH')) {
            options.body = JSON.stringify(data);
        }
        
        try {
            const response = await fetch(url, options);
            const responseData = await response.json();
            
            return {
                success: response.ok,
                status: response.status,
                data: responseData
            };
        } catch (error) {
            console.error('API Request Error:', error);
            return {
                success: false,
                status: 0,
                data: { error: 'Network error occurred' }
            };
        }
    };
    
    // Analytics tracking
    window.trackEvent = function(category, action, label = null, value = null) {
        // This would normally integrate with Google Analytics or similar
        console.log('ANALYTICS EVENT:', { category, action, label, value });
        
        // Example implementation for when a real analytics service is added:
        /*
        if (typeof gtag === 'function') {
            gtag('event', action, {
                'event_category': category,
                'event_label': label,
                'value': value
            });
        }
        */
    };
    
    // Debounce function for limiting how often a function can be called
    window.debounce = function(func, wait) {
        let timeout;
        return function(...args) {
            const context = this;
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(context, args), wait);
        };
    };
    
    // Throttle function for rate limiting
    window.throttle = function(func, limit) {
        let inThrottle;
        return function(...args) {
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    };
}); 