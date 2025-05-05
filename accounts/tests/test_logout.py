from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages

User = get_user_model()

class LogoutConfirmationTests(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.logout_url = reverse('accounts:logout')
        self.dashboard_url = reverse('accounts:dashboard')
        self.login_url = reverse('accounts:login')

    def test_logout_get_request_redirects(self):
        """Test that GET request to logout URL redirects to dashboard."""
        self.client.force_login(self.user)
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.dashboard_url)

    def test_logout_post_request_success(self):
        """Test successful logout with POST request."""
        self.client.force_login(self.user)
        response = self.client.post(self.logout_url)
        
        # Check redirect to login page
        self.assertRedirects(response, self.login_url)
        
        # Check success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have been successfully logged out.')
        
        # Verify user is logged out
        response = self.client.get(self.dashboard_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.dashboard_url}')

    def test_logout_requires_authentication(self):
        """Test that logout view requires authentication."""
        response = self.client.post(self.logout_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.logout_url}')

    def test_logout_clears_session(self):
        """Test that logout clears session data."""
        self.client.force_login(self.user)
        
        # Set some session data
        session = self.client.session
        session['test_key'] = 'test_value'
        session.save()
        
        # Perform logout
        self.client.post(self.logout_url)
        
        # Check that session is cleared
        session = self.client.session
        self.assertNotIn('test_key', session)
        self.assertNotIn('_auth_user_id', session)

    def test_logout_from_different_pages(self):
        """Test logout from different pages redirects to login."""
        self.client.force_login(self.user)
        
        # Test logout from different pages
        pages = [
            reverse('accounts:dashboard'),
            reverse('accounts:profile'),
        ]
        
        for page in pages:
            # First verify we can access the page
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)
            
            # Then test logout
            response = self.client.post(self.logout_url)
            self.assertRedirects(response, self.login_url)
            
            # Log back in for next iteration
            self.client.force_login(self.user) 