# Third-party imports...
import requests
from urllib.parse import urljoin

# Local imports...
from constants import BASE_URL

# ===============================  Method for find user ===========================
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

def get_user_by_name(strName):
    response = requests.get(urljoin(BASE_URL,'users?name=' + strName))
    if response.ok:
        return response
    else:
        return None

def get_user_by_username(strUserName):
    response = requests.get(urljoin(BASE_URL,'users?username=' + strUserName))
    if response.ok:
        return response
    else:
        return None

def get_user_by_email(strEmail):
    response = requests.get(urljoin(BASE_URL,'users?email=' + strEmail))
    if response.ok:
        return response
    else:
        return None



# =================================== Method for create new user ====================
def create_new_user():
    response = requests.post(urljoin(BASE_URL, 'users'))
    if response.ok:
        return response
    else:
        return None

def create_new_user_with_data(data):
    response = requests.post(urljoin(BASE_URL, 'users'),data=data)
    if response.ok:
        return response
    else:
        return None

# =================================== Method for delete user =========================
def delete_user_by_id(id):
    response = requests.delete(urljoin(BASE_URL,'users/' + id))
    if response.ok:
        return response
    else:
        return None

# ==================================== Method for update user ===========================
def update_user_by_id(id,data):
    response = requests.put(urljoin(BASE_URL,'users/' + id),data=data)
    if response.ok:
        return response
    else:
        return None

