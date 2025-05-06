# import unittest
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# import time


# class LogoutConfirmationTest(TestCase):
#     """Test case for the logout confirmation functionality"""
    
#     def setUp(self):
#         """Set up test data and client"""
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(
#             email='test@example.com',
#             password='testpassword123',
#             first_name='Test',
#             last_name='User'
#         )
#         self.client.login(email='test@example.com', password='testpassword123')
    
#     def test_logout_url_exists(self):
#         """Test that the logout URL exists and requires POST method"""
#         response = self.client.get(reverse('accounts:logout'))
#         self.assertEqual(response.status_code, 302)  # Redirect to login if not authenticated
        
#         # Log the user out
#         response = self.client.post(reverse('accounts:logout'))
#         self.assertEqual(response.status_code, 302)  # Redirect after logout


# class LogoutConfirmationSeleniumTest(StaticLiveServerTestCase):
#     """Test case for the logout confirmation modal using Selenium"""
    
#     @classmethod
#     def setUpClass(cls):
#         """Set up the WebDriver for Selenium tests"""
#         super().setUpClass()
#         chrome_options = Options()
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         cls.selenium = webdriver.Chrome(options=chrome_options)
#         cls.selenium.implicitly_wait(10)
    
#     @classmethod
#     def tearDownClass(cls):
#         """Clean up the WebDriver after tests"""
#         cls.selenium.quit()
#         super().tearDownClass()
    
#     def setUp(self):
#         """Set up test data and log in the user"""
#         self.user = get_user_model().objects.create_user(
#             email='test@example.com',
#             password='testpassword123',
#             first_name='Test',
#             last_name='User'
#         )
    
#     @unittest.skip("Skipping due to Selenium flakiness in CI.")
#     def test_logout_confirmation_modal(self):
#         """Test that the logout confirmation modal appears and functions correctly"""
#         # Skip this test if the WebDriver is not available
#         if not self.selenium:
#             self.skipTest("WebDriver not available")
        
#         # Log in the user
#         self.selenium.get(f'{self.live_server_url}{reverse("accounts:login")}')
#         email_input = self.selenium.find_element(By.NAME, 'email')
#         password_input = self.selenium.find_element(By.NAME, 'password')
#         email_input.send_keys('test@example.com')
#         password_input.send_keys('testpassword123')
#         self.selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
        
#         # Navigate to the dashboard
#         WebDriverWait(self.selenium, 10).until(
#             EC.url_contains('dashboard')
#         )
        
#         # Find and click the logout button
#         logout_button = self.selenium.find_element(By.XPATH, '//button[contains(text(), "Logout")]')
#         logout_button.click()
        
#         # Check if the modal appears
#         WebDriverWait(self.selenium, 10).until(
#             EC.visibility_of_element_located((By.CLASS_NAME, 'modal-backdrop'))
#         )
        
#         # Verify the modal content
#         modal_title = self.selenium.find_element(By.CLASS_NAME, 'modal-title')
#         self.assertEqual(modal_title.text, 'Logout Confirmation')
        
#         modal_body = self.selenium.find_element(By.CLASS_NAME, 'modal-body')
#         self.assertIn('Are you sure you want to log out?', modal_body.text)
        
#         # Test canceling the logout
#         cancel_button = self.selenium.find_element(By.XPATH, '//button[contains(text(), "Cancel")]')
#         cancel_button.click()
        
#         # Wait for the modal to close
#         WebDriverWait(self.selenium, 10).until(
#             EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-backdrop'))
#         )
        
#         # Verify we're still on the dashboard
#         self.assertIn('dashboard', self.selenium.current_url)
        
#         # Click logout again
#         logout_button = self.selenium.find_element(By.XPATH, '//button[contains(text(), "Logout")]')
#         logout_button.click()
        
#         # Wait for the modal to appear again
#         WebDriverWait(self.selenium, 10).until(
#             EC.visibility_of_element_located((By.CLASS_NAME, 'modal-backdrop'))
#         )
        
#         # Confirm logout this time
#         confirm_button = self.selenium.find_element(By.XPATH, '//button[contains(text(), "Yes, Logout")]')
#         confirm_button.click()
        
#         # Wait for redirect to login page
#         WebDriverWait(self.selenium, 10).until(
#             EC.url_contains('login')
#         )
        
#         # Verify we're on the login page
#         self.assertIn('login', self.selenium.current_url)


# if __name__ == '__main__':
#     unittest.main() 