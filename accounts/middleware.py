class SecurityHeadersMiddleware:
    """
    Middleware to add security headers to all responses.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
       
        # Add security headers
        csp_directives = [
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net",
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com",
            "img-src 'self' data:",
            "font-src 'self' data: https://cdnjs.cloudflare.com",
            "connect-src 'self'",
            "frame-src 'none'",
            "object-src 'none'"
        ]
        response['Content-Security-Policy'] = "; ".join(csp_directives)
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
       
        return response