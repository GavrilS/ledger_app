"""
This model holds the temp in-memory data for the command utility tool.
"""

class AppData:

    def __init__(self):
        self.users = []
        self.ledgers = {}
        self.active_user = None

    def set_active_user(self, user):
        if not user in self.users:
            print('User is not present in the list of saved users... Execute command Add User first...')
            return
        
        self.active_user = user

    def add_user(self, user):
        self.users.append(user)
    
    def add_user_ledger(self, user, ledger):
        if self.ledgers.get(user.email, None):
            confirmation = input('The user already has a ledger. Do you want to delete it and create a new one?[Yes, no]: ')
            if confirmation != 'Yes':
                return
        self.ledgers[user.email] = ledger
        print('New ledger added to user ', user_mail)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print('User removed: ', user)
            return

        print('User was not found!')

    def get_user_by_mail(self, user_mail):
        for user in self.users:
            if user.email == user_mail:
                return user
        
        print('The user was not found!')
        return None