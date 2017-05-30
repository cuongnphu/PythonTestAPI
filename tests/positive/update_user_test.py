import unittest
from src.services import *


class UpdateUserCase(unittest.TestCase):

    # Test update user by user_id
    def test_update_user_by_id(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service
        response = update_user_by_id('1', data)

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Verify that user is updated with correctly information data
        user_result = response.json()
        self.assertEqual(user_result["name"], data["name"], "data name is incorrect with input argument name")
        self.assertEqual(user_result["username"], data["username"], "data username is incorrect with input argument username")
        self.assertEqual(user_result["email"], data["email"], "data email is incorrect with input argument email")
        self.assertEqual(user_result["phone"], int(data["phone"]), "data phone is incorrect with input argument phone")
        self.assertEqual(user_result["website"], data["website"], "data website is incorrect with input argument website")



