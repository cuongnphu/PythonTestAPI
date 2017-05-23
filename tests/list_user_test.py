# Third-party import ...
import unittest
from nose.tools import assert_is_not_none,assert_equal

# Local import ....
from src.services import *

class ListUserCases(unittest.TestCase):

    def test_list_all_user(self):
        # Call the service, which will send a request to the server
        response = get_all_user()
        # If the request is sent successfully, check result is returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,200)
        print("\n Total of users:" ,len(response.json()))
        assert_equal(len(response.json()), 10)



