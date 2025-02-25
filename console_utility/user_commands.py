"""
Commands to handle user operations - creation, deletion.
"""
import ledger_app.auth.user as user

class UserCommands:

    def __init__(self, app_data):
        self.app_data = app_data

    def create_user(self):
        print('To create a new user add "Name", "Email" and "Password" when prompted:')
        user_name = input('Enter the name of the user: ')
        email = input('Enter the email of the user: ')
        password = input('Enter the user password: ')
        self.app_data.add_user(user.User(user_name, email, password))

    def delete_user(self):
        email = input('Enter the email of the user to be deleted: ')
        self.app_data.remove_user(email)