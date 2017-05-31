"""
Fun with Networks
"""

import requests



def get_users():
    response = requests.get('http://api.randomuser.me/?results=500')
    users = response.json().get('results')
    return users


def display_users():
    users = get_users()

    for user in users:
        name_data = user.get('name')
        first_name, last_name = name_data['first'], name_data['last']
        email = user.get('email')
        user_name = user.get('login')['username']
        reg_name = user.get('registered')
        date_of_birth = user.get('dob')
        print(f'Name: {first_name} {last_name}\nEmail: {email} \nUsername: {user_name} \nRegistration Date: {reg_name} \nBirth Date: {date_of_birth}\n')


display_users()