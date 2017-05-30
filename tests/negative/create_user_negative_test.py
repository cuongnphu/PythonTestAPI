import unittest
from src.services import *


class NegativeCreateUserCase(unittest.TestCase):

    # Test create user with duplicate id
    def test_create_user_with_duplicate_id(self):
        # Post data with keys 'name', 'username', 'email', 'phone', 'website'
        data = {
            "id": "1",
            "name": "cuongnp",
            "username": "cuong.nguyen",
            "email": "contact@gmail.com",
            "phone": "132456789",
            "website": "abc.com.vn"
        }

        # call the service
        response = create_new_user_with_data(data)

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error: " + str(status))

    # Test create user with none data
    def test_create_user_with_none_data(self):
        # Post data with none
        data = {

        }

        # call the service
        response = create_new_user_with_data(data)

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(500 <= status, "Server Error")
        self.assertTrue(400 <= status < 500, "Client Error: " + str(status))
