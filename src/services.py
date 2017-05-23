# Third-party imports...
import requests
from urllib.parse import urljoin

# Local imports...
from constants import BASE_URL

def get_all_user():
    response = requests.get(urljoin(BASE_URL, 'users'))
    return response

def get_user_by_id(id):
    response = requests.get(urljoin(BASE_URL, 'users?id=' + id))
    return response

def get_user_by_name(strName):
    response = requests.get(urljoin(BASE_URL,'users?name=' + strName))
    return response

def get_user_by_username(strUserName):
    response = requests.get(urljoin(BASE_URL,'users?username=' + strUserName))
    return response

def get_user_by_email(strEmail):
    response = requests.get(urljoin(BASE_URL,'users?email=' + strEmail))
    return response




def create_new_user():
    response = requests.post(urljoin(BASE_URL, 'users'))
    return response

def create_new_user_with_attribute(strAtt, strValue):
    response = requests.post(urljoin(BASE_URL, 'users'),
                             {strAtt: {strValue}})
    return response

def delete_user_by_id(id):
    response = requests.delete(urljoin(BASE_URL,'users/' + id))
    return response


def update_user_by_id(id,strName,strUserName):
    response = requests.put(urljoin(BASE_URL,'users/' + id),
                            {'name': {strName},
                             'username': {strUserName}})
    return response

