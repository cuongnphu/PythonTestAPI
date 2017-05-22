# Third-party imports...
import requests
from urllib.parse import urljoin

# Local imports...
from constants import BASE_URL

def get_all_user():
    response = requests.get(urljoin(BASE_URL, 'users'))
    if response.ok:
        return response
    else:
        return None

def get_user_by_id(id):
    response = requests.get(urljoin(BASE_URL, 'users?id=' + id))
    if response.ok:
        return response
    else:
        return None

def create_new_user():
    response = requests.post(urljoin(BASE_URL, 'users'))
    if response.ok:
        return response
    else:
        return None

def delete_user_by_id(id):
    response = requests.delete(urljoin(BASE_URL,'users/' + id))
    if response.ok:
        return response
    else:
        return None

def update_user_by_id(id,strName,strUserName):
    response = requests.put(urljoin(BASE_URL,'users/' + id),
                            {'name': {strName},
                             'username': {strUserName}
                             })
    if response.ok:
        return response
    else:
        return None

