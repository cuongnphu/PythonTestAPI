import unittest
from src.services import *


class NegativeDeleteUserCase(unittest.TestCase):

    # Test delete user with wrong user_id
    def test_negative_delete_user_with_wrong_id(self):
        # call the service
        response = delete_user_by_id('3000')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error")

        # Check status code of response API
        self.assertEqual(status, 404, "Error: status code is not 404")

    # Test delete user with none user_id
    def test_negative_delete_user_with_none_id(self):
        # call the service
        response = delete_user_by_id('')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error")

        # Check status code of response API
        self.assertEqual(status, 404, "Error: status code is not 404")

    # Test delete user with none user_id as special character
    def test_negative_delete_user_with_id_special_character(self):
        # call the service
        response = delete_user_by_id('@@')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error")

        # Check status code of response API
        self.assertEqual(status, 404, "Error: status code is not 404")
