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
        self.finance = FinCommands(self.app)
        self.user = UserCommands(self.app)

    def run(self):
        self._greeting()
        while True:
            cmd = self._get_user_input()
            final_command = cmds.command_parser(cmd)
            if final_command:
                try:
                    self._run_command(final_command)
                except Exception as e:
                    print(f"Command failed: {e}")

    def _run_command(self, cmd):
        if 'create user' in cmd:
            self.user.create_user()
        elif 'create ledger' in cmd:
            self.finance.build_user_ledger()
        elif 'create report' in cmd:
            self.finance.build_monthly_finance_report()
        elif 'delete user' in cmd:
            self.user.delete_user()
        elif 'add income' in cmd:
            self.finance.add_monthly_income()
        elif 'add expenses' in cmd:
            self.finance.add_monthly_expenditure()
        elif 'remove income' in cmd:
            self.finance.remove_monthly_income()
        elif 'remove expenses' in cmd:
            self.finance.remove_monthly_expenditure()
        elif 'show users' in cmd:
            self.user.show_users()

    def _get_user_input(self):
        user_input = input('\nEnter your command: ')
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
    