# Third-party import ...
import unittest
from nose.tools import assert_is_not_none,assert_equal

# Local import ....
from src.services import *


class DeleteUserCase(unittest.TestCase):

    def test_delete_user_by_id(self):
        # call the service, which will send a request to the server
        response = delete_user_by_id('1')
        # if the request is sent successfully, then I expect that status code of response will be 200
        print("\n Status of response is:",response.status_code)
        assert_equal(response.status_code, 200)

    def test_negative_delete_user_with_wrongID(self):
        # call the service, which will send a request to the server
        response = delete_user_by_id('30')
        # if the request is sent successfully, expected response is 404 error
        print("\n Status of response is:",response.status_code)
        assert_equal(response.status_code, 404)

