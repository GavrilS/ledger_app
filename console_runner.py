import sys
from console_utility.finance_commands import FinCommands
from console_utility.user_commands import UserCommands
from console_utility.app_data import AppData
from console_utility.commands import AVAILABLE_COMMANDS
from ledger_app.finances.ledger import Ledger
from ledger_app.finances.monthly_financing import MonthlyReport
from ledger_app.auth.user import User
import console_utility.commands as cmds

EXIT_CMDS = [
    'exit',
    'quit',
    'leave',
    'end'
]

class Engine:

    def __init__(self):
        self.app = AppData()

    def run(self):
        self._greeting()
        while True:
            cmd = self._get_user_input()

    def _get_user_input(self):
        user_input = input('Enter your command: ')
        if user_input.lower() in EXIT_CMDS:
            sys.exit()
        return user_input
    
    def _greeting(self):
        message = 'You are using the LedgerApp command line utility. For a list of available commands '
        message += 'run "help". To quit type "exit". Thank you for using the tool!'
        print(message)
        print('='*100)


if __name__=='__main__':
    engine = Engine()
    engine.run()
    