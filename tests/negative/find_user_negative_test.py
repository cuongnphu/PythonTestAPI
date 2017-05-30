import unittest
from src.services import *


class NegativeFindUserCases(unittest.TestCase):

    # Test find user by id out of Range
    def test_negative_find_user_by_id_out_of_range(self):
        # Call the service
        response = get_user_by_id('3000')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Check total user of response API
        length = len(response.json())
        self.assertEqual(length, 0, "total user is not 0")

    # Test find user with id as special character
    def test_negative_find_user_by_id_special_character(self):
        # Call the service
        response = get_user_by_id('@')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Check total user of response API
        length = len(response.json())
        self.assertEqual(length, 0, "total user is not 0")

    # Test find user by wrong name
    def test_negative_find_user_by_name_wrong(self):
        # Call the service
        response = get_user_by_name('test_wrong_name')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Check total user of response API
        length = len(response.json())
        self.assertEqual(length, 0, "total user is not 0")

    # Test find user by wrong username
    def test_negative_find_user_by_username_wrong(self):
        # Call the service
        response = get_user_by_username('test_wrong_username')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Check total user of response API
        length = len(response.json())
        self.assertEqual(length, 0, "total user is not 0")

    # Test find user by wrong email
    def test_negative_find_user_by_email_wrong(self):
        # Call the service
        response = get_user_by_email('test_wrong_email')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Check total user of response API
        length = len(response.json())
        self.assertEqual(length, 0, "total user is not 0")



