import unittest
from src.services import *


class NegativeFindUserCases(unittest.TestCase):
    def test_negative_find_user_by_id_OutOfRange(self):
        # Call the service, which will send a request to the server
        response = get_user_by_id('12')

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check content of json
        self.assertEquals(len(response.json()), 0)


    def test_negative_find_user_by_id_special_character(self):
        # Call the service, which will send a request to the server
        response = get_user_by_id('@')

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check content of json
        self.assertEquals(len(response.json()), 0)


    def test_negative_find_user_by_name_wrong(self):
        # Call the service, which will send a request to the server
        response = get_user_by_name('test_wrong_name')

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check content of json
        self.assertEquals(len(response.json()), 0)


    def test_negative_find_user_by_username_wrong(self):
        # Call the service, which will send a request to the server
        response = get_user_by_username('test_wrong_username')

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check content of json
        self.assertEquals(len(response.json()), 0)


    def test_negative_find_user_by_email_wrong(self):
        # Call the service, which will send a request to the server
        response = get_user_by_email('test_wrong_email')

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check content of json
        self.assertEquals(len(response.json()), 0)



