# Third-party import ...
import unittest

# Local import ....
from src.services import *

class ListUserCases(unittest.TestCase):

    def test_list_all_user(self):
        # Data of user at index = 5
        data_user_index_5 = {
            "id": 5,
            "name": "Chelsey Dietrich",
            "username": "Kamren",
            "email": "Lucio_Hettinger@annie.ca",
            "address": {
                "street": "Skiles Walks",
                "suite": "Suite 351",
                "city": "Roscoeview",
                "zipcode": "33263",
                "geo": {
                    "lat": "-31.8129",
                    "lng": "62.5342"
                }
            },
            "phone": "(254)954-1289",
            "website": "demarco.info",
            "company": {
                "name": "Keebler LLC",
                "catchPhrase": "User-centric fault-tolerant solution",
                "bs": "revolutionize end-to-end systems"
            }
        }

        # Call the service, which will send a request to the server
        response = get_all_user()

        # Check status code of response API
        self.assertEquals(response.status_code,200)

        # Check total user of response API
        self.assertEquals(len(response.json()), 10)

        # Verification that "name", "username, "email" ... are consistent with above data
        user_result_5 = response.json()[4]
        self.assertEquals(user_result_5["name"],data_user_index_5["name"])
        self.assertEquals(user_result_5["username"],data_user_index_5["username"])
        self.assertEquals(user_result_5["email"],data_user_index_5["email"])
        self.assertEquals(user_result_5["address"],data_user_index_5["address"])
        self.assertEquals(user_result_5["phone"],data_user_index_5["phone"])
        self.assertEquals(user_result_5["website"],data_user_index_5["website"])
        self.assertEquals(user_result_5["company"],data_user_index_5["company"])


