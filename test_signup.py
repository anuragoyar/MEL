# import requests
# import json

# # API endpoint
# url = "http://localhost:8000/api/v1/auth/signup"

# # Test data
# data = {
#     "email": "newuser@example.com",
#     "first_name": "New",
#     "last_name": "User",
#     "password": "Test@123456",
#     "password_confirm": "Test@123456",
#     "phone_number": "1234567890"
# }

# # Make the request
# response = requests.post(url, json=data)

# # Print the response
# print(f"Status Code: {response.status_code}")
# print(f"Response: {json.dumps(response.json(), indent=4)}")

# # Test with invalid data (password without special character)
# invalid_data = {
#     "email": "invalid@example.com",
#     "first_name": "Invalid",
#     "last_name": "User",
#     "password": "Test123456",
#     "password_confirm": "Test123456",
#     "phone_number": "1234567890"
# }

# # Make the request with invalid data
# invalid_response = requests.post(url, json=invalid_data)

# # Print the response
# print("\nInvalid Data Test:")
# print(f"Status Code: {invalid_response.status_code}")
# print(f"Response: {json.dumps(invalid_response.json(), indent=4)}")

# # Test with duplicate email
# duplicate_data = {
#     "email": "newuser@example.com",  # Same email as first request
#     "first_name": "Duplicate",
#     "last_name": "User",
#     "password": "Test@123456",
#     "password_confirm": "Test@123456",
#     "phone_number": "1234567890"
# }

# # Make the request with duplicate email
# duplicate_response = requests.post(url, json=duplicate_data)

# # Print the response
# print("\nDuplicate Email Test:")
# print(f"Status Code: {duplicate_response.status_code}")
# print(f"Response: {json.dumps(duplicate_response.json(), indent=4)}") 