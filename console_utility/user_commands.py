"""
Commands to handle user operations - creation, deletion.
"""

class UserCommands:

    def __init__(self):
        pass

    def create_user(self):
        print('To create a new user add "Name", "Email" and "Password" when prompted:')
        user_name = input('Enter the name of the user: ')
        email = input('Enter the email of the user: ')
        password = input('Enter the user password: ')
        return {'name': user_name, 'email': email, 'password': password}

    def delete_user(self):
        pass