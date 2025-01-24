"""
This is a model for the income/expenditures for a person as a total.
"""

class TotalFinanceCard:

    def __init__(self, user=None, finance_history=None):
        self._user = user
        self._finance_history = finance_history

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if not value:
            raise Exception('User must be specified!')
        self._user = value
    
    @property
    def finances(self):
        return self._finance_history

    @finances.setter
    def finances(self, value):
        if not value:
            raise Exception('Missing user finances...')
        
        self._finance_history = value