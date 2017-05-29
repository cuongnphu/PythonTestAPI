import unittest
from src.services import *


class FindUserCases(unittest.TestCase):

    # Test find user by Id
    def test_find_user_by_id(self):
        # Call the service
        response = get_user_by_id('1')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Check total user of response API
        length = len(response.json())
        self.assertEqual(length, 1, "total user is not 1")

        # Get last user
        user_result = response.json()[length - 1]

        # Check data user of response API
        self.assertEqual(user_result["id"], 1 , "incorrect user id")
        self.assertIsNotNone(user_result["name"], "name is None")
        self.assertIsNotNone(user_result["username"], "username is None")
        self.assertIsNotNone(user_result["email"], "email is None")
        self.assertIsNotNone(user_result["address"], "address is None")
        self.assertIsNotNone(user_result["phone"], "phone is None")
        self.assertIsNotNone(user_result["website"], "website is None")
        self.assertIsNotNone(user_result["company"], "company is None")

    # Test find user by name
    def test_find_user_by_name(self):
        # Call the service
        response = get_user_by_name('Leanne Graham')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Get last user
        length = len(response.json())
        user_result = response.json()[length - 1]

        # Check data user of response API
        self.assertEqual(user_result["name"], 'Leanne Graham' , "incorrect name")
        self.assertIsNotNone(user_result["id"], "id is None")
        self.assertIsNotNone(user_result["username"], "username is None")
        self.assertIsNotNone(user_result["email"], "email is None")
        self.assertIsNotNone(user_result["address"], "address is None")
        self.assertIsNotNone(user_result["phone"], "phone is None")
        self.assertIsNotNone(user_result["website"], "website is None")
        self.assertIsNotNone(user_result["company"], "company is None")

    # Test find user by username
    def test_find_user_by_username(self):
        # Call the service
        response = get_user_by_username('Bret')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Get last user
        length = len(response.json())
        user_result = response.json()[length - 1]

        # Check data user of response API
        self.assertEqual(user_result["username"], 'Bret' , "incorrect username")
        self.assertIsNotNone(user_result["id"], "id is None")
        self.assertIsNotNone(user_result["name"], "name is None")
        self.assertIsNotNone(user_result["email"], "email is None")
        self.assertIsNotNone(user_result["address"], "address is None")
        self.assertIsNotNone(user_result["phone"], "phone is None")
        self.assertIsNotNone(user_result["website"], "website is None")
        self.assertIsNotNone(user_result["company"], "company is None")

    # Test find user by email
    def test_find_user_by_email(self):
        # Call the service
        response = get_user_by_email('Sincere@april.biz')

        # Get response status code
        status = response.status_code

        # Check status code in range error
        self.assertFalse(400 <= status < 500, "Client Error")
        self.assertFalse(500 <= status, "Server Error")

        # Check status code of response API
        self.assertEqual(status, 200, "status code is not 200")

        # Get last user
        length = len(response.json())
        user_result = response.json()[length - 1]

        # Check data user of response API
        self.assertEqual(user_result["email"], 'Sincere@april.biz' , "incorrect email")
        self.assertIsNotNone(user_result["id"], "id is None")
        self.assertIsNotNone(user_result["name"], "name is None")
        self.assertIsNotNone(user_result["username"], "username is None")
        self.assertIsNotNone(user_result["address"], "address is None")
        self.assertIsNotNone(user_result["phone"], "phone is None")
        self.assertIsNotNone(user_result["website"], "website is None")
        self.assertIsNotNone(user_result["company"], "company is None")



