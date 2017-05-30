import unittest
from src.services import *


class NegativeUpdateUserCase(unittest.TestCase):

    # Test update user with wrong user_id
    def test_update_user_with_id_out_of_range(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service
        response = update_user_by_id('3000', data)

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error")

        # Check status code of response API
        self.assertEqual(status, 404, "Error: status code is not 404")

    # Test update user with null user_id
    def test_update_user_with_id_null(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service
        response = update_user_by_id('', data)

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error")

        # Check status code of response API
        self.assertEqual(status, 404, "Error: status code is not 404")

    # Test update user with user_id as special character
    def test_update_user_with_id_special_character(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service
        response = update_user_by_id('@@', data)

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error")

        # Check status code of response API
        self.assertEqual(status, 404, "Error: status code is not 404")



