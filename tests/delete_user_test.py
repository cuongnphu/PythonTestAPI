# Third-party import ...
import unittest

# Local import ....
from src.services import *


class DeleteUserCase(unittest.TestCase):

    def test_delete_user_by_id(self):
        # call the service, which will send a request to the server
        response = delete_user_by_id('1')

        # Check status code of response will be 200
        self.assertEqual(response.status_code, 200)

    def test_negative_delete_user_with_wrongID(self):
        # call the service, which will send a request to the server
        response = delete_user_by_id('30')

        # Check status code of response API is 404 error
        self.assertEqual(response, None)

