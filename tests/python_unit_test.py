# Third-party import ...
import unittest
from nose.tools import assert_is_not_none,assert_equal

# Local import ....
from utils.services import *

# Running unit test
class MyTestCase(unittest.TestCase):

    def test_list_all_user(self):
        # Call the service, which will send a request to the server
        response = get_all_user()
        # If the request is sent successfully, then expected result is 10
        print("\n List all user:" ,len(response.json()))
        assert_equal(len(response.json()), 10)

    def test_find_user_by_id(self):
        # Call the service, which will send a request to the server
        response = get_user_by_id('1')
        # If the request is sent successfully, then I expect a response to be returned
        assert_is_not_none(response)

    def test_create_new_user(self):
        # call the service, which will send a request to the server
        response = create_new_user()
        # if the request is sent successfully, then I expect that result will be current user + 1
        assert_equal(response.json()["id"],len(get_all_user().json()) + 1)

    def test_delete_user_by_id(self):
        # call the service, which will send a request to the server
        response = delete_user_by_id('1')
        # if the request is sent successfully, then I expect that status code of response will be 200
        assert_equal(response.status_code, 200)

    def test_update_user_by_id(self):
        # call the service, which will send a request to the server
        response = update_user_by_id('1','cuongnp','wet')
        # if the request is sent successfully, then I expect that user by ID will be updated
        assert_equal(response.json()["name"],'cuongnp')
        assert_equal(response.json()["username"],'wet')









