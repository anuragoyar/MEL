from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime

User = get_user_model()

class ProfileViewTests(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            date_joined=timezone.make_aware(datetime(2023, 1, 1))
        )
        self.profile_url = reverse('accounts:profile')
        self.login_url = reverse('accounts:login')

    def test_profile_view_requires_login(self):
        """Test that profile view requires authentication."""
        # Try accessing profile without login
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(self.login_url))

        # Login and try again
        self.client.login(username='testuser@example.com', password='testpass123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_uses_correct_template(self):
        """Test that profile view uses the correct template."""
        self.client.login(username='testuser@example.com', password='testpass123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_profile_context_data(self):
        """Test that profile view provides correct context data."""
        self.client.login(username='testuser@example.com', password='testpass123')
        response = self.client.get(self.profile_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertEqual(response.context['page_title'], 'Profile')
        self.assertEqual(
            response.context['date_joined'],
            self.user.date_joined.strftime('%B %d, %Y')
        )

    def test_profile_content(self):
        """Test that profile page displays correct user information."""
        self.client.login(username='testuser@example.com', password='testpass123')
        response = self.client.get(self.profile_url)
        
        content = response.content.decode()
        self.assertIn('Test User', content)  # Full name
        self.assertIn('testuser@example.com', content)  # Email
        self.assertIn('January 01, 2023', content)  # Date joined

    def test_profile_with_minimal_user_info(self):
        """Test profile display with minimal user information."""
        minimal_user = User.objects.create_user(
            email='minimal@example.com',
            password='testpass123'
        )
        
        self.client.login(username='minimal@example.com', password='testpass123')
        response = self.client.get(self.profile_url)
        
        content = response.content.decode()
        self.assertIn('Not provided', content)  # Default text for missing name
        self.assertIn('minimal@example.com', content)

    def test_profile_navigation_links(self):
        """Test that profile page contains correct navigation links."""
        self.client.login(username='testuser@example.com', password='testpass123')
        response = self.client.get(self.profile_url)
        
        content = response.content.decode()
        dashboard_url = reverse('accounts:dashboard')
        self.assertIn(f'href="{dashboard_url}"', content)
        self.assertIn('class="active"', content)  # Profile link should be active 