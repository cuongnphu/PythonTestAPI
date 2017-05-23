# Third-party import ...
import unittest
from nose.tools import assert_is_not_none,assert_equal

# Local import ....
from src.services import *


class CreateUserCase(unittest.TestCase):

    def test_create_new_user(self):
        # call the service, which will send a request to the server
        response = create_new_user()
        # if the request is sent successfully, then I expect that result will be current user + 1
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,201)
        print("\n ID of user is :", response.json()["id"])
        assert_equal(response.json()["id"],len(get_all_user().json()) + 1)

    def test_create_user_with_attribute(self):
        # call the service, which will send a request to the server
        response = create_new_user_with_attribute('name','Cuong Nguyen')
        # if the request is sent successfully, then I expect that result will be current user + 1
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,201)
        print("\n ID of user is :", response.json()["id"])
        assert_equal(response.json()["id"],len(get_all_user().json()) + 1)
        print("\n Name of user is :", response.json()["name"])
        assert_equal(response.json()["name"],'Cuong Nguyen')



class NegativeCreateUserCase(unittest.TestCase):

    def test_create_user_with_duplicateID(self):
        # call the service, which will send a request to the server
        response = create_new_user_with_attribute('id','1')
        # if the request is sent successfully, expected result is 404
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,404)


