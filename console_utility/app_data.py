"""
This model holds the temp in-memory data for the command utility tool.
"""
import ledger_app.finances.ledger as ledger

class AppData:

    def __init__(self):
        self.users = []
        self.ledgers = {}
        self.active_user = None

    def change_active_user(self):
        self.list_user_mails()
        user_mail = input('Provide user email for the new active user: ')
        user = self.get_user_by_mail(user_mail)
        self.set_active_user(user)

    def set_active_user(self, user):
        if not user in self.users:
            print('User is not present in the list of saved users... Execute command Add User first...')
            return
        
        self.active_user = user
        print('New active user set: ', user)
    
    def show_active_user(self):
        print(f"The current active user is: {self.active_user}")

    def add_user(self, user):
        self.users.append(user)
        print('User added!')

    def remove_user(self, user_email):
        for user in self.users:
            if user.email == user_email:
                self.users.remove(user)
                print('User removed!')
                return
        
        print('User with this email was not found...')
    
    def add_user_ledger(self, user, ledger):
        if self.ledgers.get(user.email, None):
            confirmation = input('The user already has a ledger. Do you want to delete it and create a new one?[Yes, no]: ')
            if confirmation != 'Yes':
                return
        self.ledgers[user.email] = ledger
        print('New ledger added to user ', user.email)

    def show_user_ledger(self):
        self.verify_active_user()
        print(self.ledgers[self.active_user.email])

    def get_user_monthly_report(self, year, month):
        self.verify_active_user_ledger()
        ledger = self.ledgers[self.active_user]
        for report in ledger.finances:
            if report.year == year and report.month == month:
                return report

    def get_user_by_mail(self, user_mail):
        for user in self.users:
            if user.email == user_mail:
                return user
        
        print('The user was not found!')
        return None
    
    def list_user_mails(self):
        print('List of active users: ')
        for user in self.users:
            print(user)

    def verify_active_user_ledger(self):
        if self.verify_active_user():
            if not self.ledgers.get(self.active_user, None):
                user_ledger = ledger.Ledger(self.active_user)
                self.add_user_ledger(self.active_user, user_ledger)
            
            return True  
        return False

    def verify_active_user(self):
        try:
            if not self.active_user:
                self.list_user_mails()
                get_user_mail = input('There is no active user currently. Provide an existing user email to make it active: ')
                user = self.get_user_by_mail(get_user_mail)
                if not user:
                    return False
                self.set_active_user(user)
            
            return True
        except Exception as e:
            print(f"Issue verifying active user: {e}")
            return False