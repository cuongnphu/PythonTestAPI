import unittest
from src.services import *


class CreateUserCase(unittest.TestCase):

    # Test create new user
    def test_create_new_user(self):
        # Get current user
        previous_length = len(get_all_user().json())

        # call the service
        response = create_new_user()

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 201, "status code is not 201")

        # Check current user will be increased
        user_result = response.json()
        current_length = len(get_all_user().json())
        self.assertIsNotNone(user_result["id"], "user_id is None")
        self.assertGreaterEqual(previous_length,current_length, "current user is not increased")

    # Test create new user with data
    def test_create_user_with_data(self):
        # Post data with keys 'name', 'username', 'email', 'phone', 'website'
        data = {
            "name": "cuongnp",
            "username": "cuong.nguyen",
            "email": "contact@gmail.com",
            "phone": "132456789",
            "website": "abc.com.vn"
        }

        # Get current user
        previous_length = len(get_all_user().json())

        # call the service
        response = create_new_user_with_data(data)

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 201, "status code is not 201")

        # Check current user will be increased
        user_result = response.json()
        current_length = len(get_all_user().json())
        self.assertIsNotNone(user_result["id"], "user_id is None")
        self.assertGreaterEqual(previous_length,current_length, "current user is not increased")

        # Verify that user is created with correctly information data
        self.assertEqual(user_result["name"], data["name"], "data name is incorrect with input argument name")
        self.assertEqual(user_result["username"], data["username"], "data username is incorrect with input argument username")
        self.assertEqual(user_result["email"], data["email"], "data email is incorrect with input argument email")
        self.assertEqual(user_result["phone"], int(data["phone"]), "data phone is incorrect with input argument phone")
        self.assertEqual(user_result["website"], data["website"], "data website is incorrect with input argument website")






