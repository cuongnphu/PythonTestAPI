# Third-party import ...
import unittest

from nose.tools import assert_is_not_none,assert_equal

# Local import ....
from src.services import *


class FindUserCases(unittest.TestCase):

    def test_find_user_by_id(self):
        # Call the service, which will send a request to the server
        response = get_user_by_id('1')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,200)
        print("\n Total of users:",len(response.json()))
        assert_equal(len(response.json()), 1)
        print("\n ID of user is :", response.json()[0]["id"])
        assert_equal(response.json()[0]["id"], 1)


    def test_find_user_by_name(self):
        # Call the service, which will send a request to the server
        response = get_user_by_name('Leanne Graham')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,200)
        print("\n Total of users:",len(response.json()))
        assert_equal(len(response.json()), 1)
        print("\n Name of user is :", response.json()[0]["name"])
        assert_equal(response.json()[0]["name"], 'Leanne Graham')


    def test_find_user_by_username(self):
        # Call the service, which will send a request to the server
        response = get_user_by_username('Bret')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,200)
        print("\n Total of users:",len(response.json()))
        assert_equal(len(response.json()), 1)
        print("\n Username of user is:",response.json()[0]["username"])
        assert_equal(response.json()[0]["username"],'Bret')


    def test_find_user_by_email(self):
        # Call the service, which will send a request to the server
        response = get_user_by_email('Sincere@april.biz')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,200)
        print("\n Total of users:",len(response.json()))
        assert_equal(len(response.json()), 1)
        print("\n Username of user is:",response.json()[0]["email"])
        assert_equal(response.json()[0]["email"],'Sincere@april.biz')




class NegativeFindUserCases(unittest.TestCase):

    def test_negative_find_user_by_id_OutOfRange(self):
        # Call the service, which will send a request to the server
        response = get_user_by_id('12')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code,200)
        assert_equal(response.json(),[])


    def test_negative_find_user_by_name_wrong(self):
        # Call the service, which will send a request to the server
        response = get_user_by_name('test')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code, 200)
        assert_equal(response.json(),[])


    def test_negative_find_user_by_username_wrong(self):
        # Call the service, which will send a request to the server
        response = get_user_by_username('test')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code, 200)
        assert_equal(response.json(),[])


    def test_negative_find_user_by_email_wrong(self):
        # Call the service, which will send a request to the server
        response = get_user_by_email('test')
        # If the request is sent successfully, then I expect a response to be returned
        print("\n Status of response is: ",response.status_code)
        assert_equal(response.status_code, 200)
        assert_equal(response.json(),[])
