"""
Commands to handle user operations - creation, deletion.
"""
import ledger_app.auth.user as user

class UserCommands:

    def __init__(self, app_data):
        self.app_data = app_data

    def create_user(self):
        try:
            print('To create a new user add "Name", "Email" and "Password" when prompted:')
            user_name = input('Enter the name of the user: ')
            email = input('Enter the email of the user: ')
            password = input('Enter the user password: ')
            self.app_data.add_user(user.User(name=user_name, password=password, email=email))
        except Exception as e:
            print(f"Error trying to create a new user: \n{e}")

    def delete_user(self):
        email = input('Enter the email of the user to be deleted: ')
        self.app_data.remove_user(email)

    def show_users(self):
        self.app_data.list_user_mails()

    def change_user(self):
        try:
            self.app_data.change_active_user()
            print('The active user was changed!')
        except Exception as e:
            print(f"The user couldn't be switched: \n{e}")
    
    def show_active_user(self):
        try:
            self.app_data.show_active_user()
        except Exception as e:
            print(f"Couldn't show the active user: \n{e}")