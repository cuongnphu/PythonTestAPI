# Third-party import ...
import unittest

# Local import ....
from src.services import *


class UpdateUserCase(unittest.TestCase):

    def test_update_user_by_id(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service, which will send a request to the server
        response = update_user_by_id('1', data)
        user_result = response.json()

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check data user of response API
        self.assertEqual(user_result["name"],data["name"])
        self.assertEqual(user_result["username"],data["username"])
        self.assertEqual(user_result["email"],data["email"])
        self.assertEqual(user_result["phone"],int(data["phone"]))
        self.assertEqual(user_result["website"],data["website"])


class NegativeUpdateUserCase(unittest.TestCase):

    def test_update_user_with_id_outofrange(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service, which will send a request to the server
        response = update_user_by_id('30', data)

        # Check status code of response API
        self.assertEqual(response, None)


    def test_update_user_with_id_null(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service, which will send a request to the server
        response = update_user_by_id('', data)

        # Check status code of response API
        self.assertEqual(response, None)

    def test_update_user_with_id_special_character(self):
        data = {
            "name": "cuongnp",
            "username": "wet",
            "email": "contact@hehe.com",
            "phone": "121321321",
            "website": "abc.com.vn"
        }

        # call the service, which will send a request to the server
        response = update_user_by_id('@', data)

        # Check status code of response API
        self.assertEqual(response, None)
