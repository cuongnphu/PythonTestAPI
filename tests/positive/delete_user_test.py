import unittest
from src.services import *


class DeleteUserCase(unittest.TestCase):

    # Test delete user by user_id
    def test_delete_user_by_id(self):
        # Get current user
        previous_length = len(get_all_user().json())

        # call the service
        response = delete_user_by_id('1')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "Error: status code is not 200")

        # Check current user will be increased
        current_length = len(get_all_user().json())
        self.assertTrue(previous_length > current_length, "Error: user is not deleted")



