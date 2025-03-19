from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import User

class DashboardViewTest(TestCase):
    """
    Test cases for the dashboard view
    """
    
    def setUp(self):
        """
        Set up test data
        """
        self.client = Client()
        self.dashboard_url = reverse('accounts:dashboard')
        self.login_url = '/'  # The login page is at the root URL
        
        # Create a test user
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='SecurePassword123!',
            first_name='Test',
            last_name='User'
        )
    
    def test_dashboard_access_authenticated(self):
        """
        Test that an authenticated user can access the dashboard
        """
        # Login the user
        self.client.login(username='testuser@example.com', password='SecurePassword123!')
        
        # Access the dashboard
        response = self.client.get(self.dashboard_url)
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'accounts/dashboard.html')
        
        # Check that the user's name is in the response
        self.assertContains(response, 'Test')
    
    def test_dashboard_access_unauthenticated(self):
        """
        Test that an unauthenticated user is redirected to the login page
        """
        # Access the dashboard without logging in
        response = self.client.get(self.dashboard_url)
        
        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        
        # Check that the redirect URL contains the login URL
        self.assertTrue(response.url.startswith(self.login_url))
    
    def test_dashboard_context(self):
        """
        Test that the dashboard view provides the correct context
        """
        # Login the user
        self.client.login(username='testuser@example.com', password='SecurePassword123!')
        
        # Access the dashboard
        response = self.client.get(self.dashboard_url)
        
        # Check that the context contains the user
        self.assertEqual(response.context['user'], self.user)
        
        # Check that the context contains the page title
        self.assertEqual(response.context['page_title'], 'Dashboard')
    
    def test_dashboard_template_content(self):
        """
        Test that the dashboard template contains the expected elements
        """
        # Login the user
        self.client.login(username='testuser@example.com', password='SecurePassword123!')
        
        # Access the dashboard
        response = self.client.get(self.dashboard_url)
        
        # Check for key elements in the HTML
        self.assertContains(response, '<div class="dashboard-container">')
        self.assertContains(response, '<header class="dashboard-header">')
        self.assertContains(response, '<aside class="sidebar">')
        self.assertContains(response, '<main class="main-content">')
        self.assertContains(response, '<footer class="dashboard-footer">')
        
        # Check for widget elements
        self.assertContains(response, '<div class="widget">')
        self.assertContains(response, '<div class="widget-header">')
        self.assertContains(response, '<div class="widget-content">')
    
    def test_logout_functionality(self):
        """
        Test that the logout functionality works correctly
        """
        # Login the user
        self.client.login(username='testuser@example.com', password='SecurePassword123!')
        
        # Access the dashboard to verify login
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        
        # Perform logout
        logout_url = reverse('accounts:logout')
        response = self.client.post(logout_url)
        
        # Check that the response is a redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(self.login_url))
        
        # Try to access dashboard after logout
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(self.login_url))
    
    def test_logout_requires_post(self):
        """
        Test that logout only works with POST method
        """
        # Login the user
        self.client.login(username='testuser@example.com', password='SecurePassword123!')
        
        # Try to logout with GET request
        logout_url = reverse('accounts:logout')
        response = self.client.get(logout_url)
        
        # Should be redirected to dashboard
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/')
        
        # Verify still logged in by accessing dashboard
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200) 