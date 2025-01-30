"""
This model holds the temp in-memory data for the command utility tool.
"""

class AppData:

    def __init__(self):
        self.users = []
        self.ledgers = {}

    def add_user(self, user):
        self.users.append(user)
    
    def add_user_ledger(self, user_mail, ledger):
        if self.ledgers.get(user_mail, None):
            confirmation = input('The user already has a ledger. Do you want to delete it and create a new one?[Yes, no]: ')
            if confirmation != 'Yes':
                return
        self.ledgers[user_mail] = ledger
        print('New ledger added to user ', user_mail)

    def remove_user(self, user_email):
        for user in self.users:
            if user.email == user_email:
                self.users.remove(user)
                print('User removed: ', user)
                return

        print('User was not found!')