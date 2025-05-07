# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.utils import timezone
# from datetime import datetime

# User = get_user_model()

# class ProfileViewTests(TestCase):
#     def setUp(self):
#         """Set up test data."""
#         self.client = Client()
#         self.profile_url = reverse('accounts:profile')
#         self.login_url = reverse('accounts:login')
        
#         # Create a test user
#         self.user = User.objects.create_user(
#             email='test@example.com',
#             password='testpass123',
#             first_name='Test',
#             last_name='User',
#             date_joined=timezone.make_aware(datetime(2023, 1, 1))
#         )

#     def test_profile_url_exists(self):
#         """Test that profile URL exists and returns correct template."""
#         self.client.force_login(self.user)
#         response = self.client.get(self.profile_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'accounts/profile.html')

#     def test_profile_requires_authentication(self):
#         """Test that profile page requires authentication."""
#         # Try accessing without login
#         response = self.client.get(self.profile_url)
#         self.assertRedirects(
#             response, 
#             f'{self.login_url}?next={self.profile_url}'
#         )

#     def test_profile_displays_user_info(self):
#         """Test that profile page displays correct user information."""
#         self.client.force_login(self.user)
#         response = self.client.get(self.profile_url)
        
#         # Check that user info is in context
#         self.assertEqual(response.context['user'], self.user)
#         self.assertEqual(
#             response.context['date_joined'],
#             'January 01, 2023'
#         )
        
#         # Check content in response
#         content = response.content.decode()
#         self.assertIn('Test User', content)  # Full name
#         self.assertIn('test@example.com', content)  # Email
#         self.assertIn('January 01, 2023', content)  # Date joined

#     def test_profile_handles_missing_name(self):
#         """Test that profile page handles missing name gracefully."""
#         # Create user without name
#         user_no_name = User.objects.create_user(
#             email='noname@example.com',
#             password='testpass123'
#         )
        
#         self.client.force_login(user_no_name)
#         response = self.client.get(self.profile_url)
        
#         # Check that default value is used
#         self.assertIn('Not provided', response.content.decode())

#     def test_profile_page_context(self):
#         """Test that profile page contains all required context variables."""
#         self.client.force_login(self.user)
#         response = self.client.get(self.profile_url)
        
#         self.assertIn('user', response.context)
#         self.assertIn('page_title', response.context)
#         self.assertIn('date_joined', response.context)
        
#         self.assertEqual(response.context['page_title'], 'Profile')

#     def test_profile_navigation(self):
#         """Test navigation links on profile page."""
#         self.client.force_login(self.user)
#         response = self.client.get(self.profile_url)
        
#         content = response.content.decode()
#         dashboard_url = reverse('accounts:dashboard')
#         logout_url = reverse('accounts:logout')
        
#         # Check that navigation links exist
#         self.assertIn(f'href="{dashboard_url}"', content)
#         self.assertIn(f'action="{logout_url}"', content)

#     def test_special_characters_handling(self):
#         """Test that profile page handles special characters correctly."""
#         # Create user with special characters in name
#         user_special = User.objects.create_user(
#             email='special@example.com',
#             password='testpass123',
#             first_name='Tést',
#             last_name='Üser'
#         )
        
#         self.client.force_login(user_special)
#         response = self.client.get(self.profile_url)
        
#         content = response.content.decode()
#         self.assertIn('Tést Üser', content) 