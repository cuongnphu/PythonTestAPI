import unittest
from src.services import *


class ListUserCases(unittest.TestCase):

    # Test list all user
    def test_list_all_user(self):
        # Call the service
        response = get_all_user()

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check response status code
        self.assertEqual(status, 200,"status code is not 200")

        # Check total users
        length = len(response.json())
        self.assertGreaterEqual(length, 0,"Total user is 0")

        # Get last user
        user_result = response.json()[length - 1]

        # Verification that "name", "username, "email" ... with last user
        self.assertIsNotNone(user_result["name"],"name is None")
        self.assertIsNotNone(user_result["username"],"username is None")
        self.assertIsNotNone(user_result["email"],"email is None")
        self.assertIsNotNone(user_result["address"],"address is None")
        self.assertIsNotNone(user_result["phone"],"phone is None")
        self.assertIsNotNone(user_result["website"],"website is None")
        self.assertIsNotNone(user_result["company"],"company is None")


