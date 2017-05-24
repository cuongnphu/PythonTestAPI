# Third-party import ...
import unittest

# Local import ....
from src.services import *


class FindUserCases(unittest.TestCase):
    def test_find_user_by_id(self):
        # Data of user at index = 0
        data_user_index_0 = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }

        # Call the service, which will send a request to the server
        response = get_user_by_id('1')
        user_result = response.json()[0]

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check total user of response API
        self.assertEquals(len(response.json()), 1)

        # Check data user of response API
        self.assertEquals(user_result["id"], 1)
        self.assertIsNotNone(user_result["name"])
        self.assertIsNotNone(user_result["username"])
        self.assertIsNotNone(user_result["email"])
        self.assertIsNotNone(user_result["address"])
        self.assertIsNotNone(user_result["phone"])
        self.assertIsNotNone(user_result["website"])
        self.assertIsNotNone(user_result["company"])

    def test_find_user_by_name(self):
        # Data of user at index = 0
        data_user_index_0 = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }

        # Call the service, which will send a request to the server
        response = get_user_by_name('Leanne Graham')
        user_result = response.json()[0]

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check total user of response API
        self.assertEquals(len(response.json()), 1)

        # Check data user of response API
        self.assertEquals(user_result["name"], 'Leanne Graham')
        self.assertIsNotNone(user_result["id"])
        self.assertIsNotNone(user_result["username"])
        self.assertIsNotNone(user_result["email"])
        self.assertIsNotNone(user_result["address"])
        self.assertIsNotNone(user_result["phone"])
        self.assertIsNotNone(user_result["website"])
        self.assertIsNotNone(user_result["company"])

    def test_find_user_by_username(self):
        # Data of user at index = 0
        data_user_index_0 = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }

        # Call the service, which will send a request to the server
        response = get_user_by_username('Bret')
        user_result = response.json()[0]

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check total user of response API
        self.assertEquals(len(response.json()), 1)

        # Check data user of response API
        self.assertEquals(user_result["username"], 'Bret')
        self.assertIsNotNone(user_result["id"])
        self.assertIsNotNone(user_result["name"])
        self.assertIsNotNone(user_result["email"])
        self.assertIsNotNone(user_result["address"])
        self.assertIsNotNone(user_result["phone"])
        self.assertIsNotNone(user_result["website"])
        self.assertIsNotNone(user_result["company"])

    def test_find_user_by_email(self):
        # Data of user at index = 0
        data_user_index_0 = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }

        # Call the service, which will send a request to the server
        response = get_user_by_email('Sincere@april.biz')
        user_result = response.json()[0]

        # Check status code of response API
        self.assertEquals(response.status_code, 200)

        # Check total user of response API
        self.assertEquals(len(response.json()), 1)

        # Check data user of response API
        self.assertEquals(user_result["email"], 'Sincere@april.biz')
        self.assertIsNotNone(user_result["id"])
        self.assertIsNotNone(user_result["name"])
        self.assertIsNotNone(user_result["username"])
        self.assertIsNotNone(user_result["address"])
        self.assertIsNotNone(user_result["phone"])
        self.assertIsNotNone(user_result["website"])
        self.assertIsNotNone(user_result["company"])


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
