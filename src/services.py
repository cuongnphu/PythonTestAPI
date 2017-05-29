import requests
from urllib.parse import urljoin
from constants import BASE_URL


# Get list users
def get_all_user():
    # Create URL for request
    all_user_url = urljoin(BASE_URL, 'users')

    # Return response
    return requests.get(all_user_url)


# Get user by id
def get_user_by_id(user_id):
    # Create URL for request
    user_by_id_url = urljoin(BASE_URL, 'users?id=' + user_id)

    # Return response
    return requests.get(user_by_id_url)


# Get user by name
def get_user_by_name(str_name):
    # Create URL for request
    user_by_name_url = urljoin(BASE_URL, 'users?name=' + str_name)

    # Return response
    return requests.get(user_by_name_url)


# Get user by username
def get_user_by_username(str_username):
    # Create URL for request
    user_by_username_url = urljoin(BASE_URL, 'users?username=' + str_username)

    # Return response
    return requests.get(user_by_username_url)


# Get user by email
def get_user_by_email(str_email):
    # Create URL for request
    user_by_email_url = urljoin(BASE_URL, 'users?email=' + str_email)

    # Return response
    return requests.get(user_by_email_url)


# Create new user without data
def create_new_user():
    # Create URL for request
    create_new_user_url = urljoin(BASE_URL, 'users')

    # Return response
    return requests.post(create_new_user_url)


# Create new user with data
def create_new_user_with_data(data):
    # Create URL for request
    create_new_user_url = urljoin(BASE_URL, 'users')

    # Return response
    return requests.post(create_new_user_url , data=data)


# Delete user by id
def delete_user_by_id(user_id):
    # Create URL for request
    delete_user_url = urljoin(BASE_URL,'users/' + user_id)

    # Return response
    return requests.delete(delete_user_url)


# Update user by id
def update_user_by_id(user_id, data):
    # Create URL for request
    update_user_url = urljoin(BASE_URL,'users/' + user_id)

    # Return response
    return requests.put(update_user_url, data=data)



