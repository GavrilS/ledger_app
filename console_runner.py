from console_utility.finance_commands import build_user_ledger, build_monthly_finance_report
from console_utility.user_commands import UserCommands
from console_utility.app_data import AppData
from console_utility.commands import AVAILABLE_COMMANDS
from ledger_app.finances.ledger import Ledger
from ledger_app.finances.monthly_financing import MonthlyReport
from ledger_app.auth.user import User

class Engine:

    def __init__(self):
        self.app = AppData()

    def run(self):
        while True:
            pass
    
    def help(self):
        print('This is a list of supported commands:')
        for k, v in AVAILABLE_COMMANDS.items():
            print(cmd)
            print('-'*80)



if __name__=='__main__':
    engine = Engine()
    engine.run()
    