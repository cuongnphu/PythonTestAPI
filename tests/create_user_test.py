# Third-party import ...
import unittest

# Local import ....
from src.services import *


class CreateUserCase(unittest.TestCase):

    def test_create_new_user(self):
        # call the service, which will send a request to the server
        response = create_new_user()
        user_result = response.json()

        # Check status code of response API
        self.assertEquals(response.status_code,201)

        # Check current user will be increased by one
        self.assertEquals(user_result["id"],len(get_all_user().json()) + 1)

    def test_create_user_with_data(self):
        #Post data with keys 'name', 'username', 'email', 'phone', 'website'
        data = {
            "name": "cuongnp",
            "username": "cuong.nguyen",
            "email": "contact@gmail.com",
            "phone": "132456789",
            "website": "abc.com.vn"
        }

        # call the service, which will send a request to the server
        response = create_new_user_with_data(data)
        user_result = response.json()

        # Check status code of response API
        self.assertEquals(response.status_code,201)

        # Verify that user is created via all information are correct
        self.assertEquals(response.json()["id"],len(get_all_user().json()) + 1)
        self.assertEquals(user_result["name"], data["name"])
        self.assertEquals(user_result["username"], data["username"])
        self.assertEquals(user_result["email"], data["email"])
        self.assertEquals(user_result["phone"], int(data["phone"]))
        self.assertEquals(user_result["website"], data["website"])



class NegativeCreateUserCase(unittest.TestCase):

    def test_create_user_with_duplicate_id(self):
        #Post data with keys 'name', 'username', 'email', 'phone', 'website'
        data = {
            "id": "1",
            "name": "cuongnp",
            "username": "cuong.nguyen",
            "email": "contact@gmail.com",
            "phone": "132456789",
            "website": "abc.com.vn"
        }

        # call the service, which will send a request to the server
        response = create_new_user_with_data(data)

        # Check status code of response API is 404
        self.assertEquals(response.status_code,404)


