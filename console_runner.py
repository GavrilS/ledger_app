from console_utility.finance_commands import build_user_ledger, build_monthly_finance_report
from console_utility.user_commands import UserCommands
from console_utility.app_data import AppData
from console_utility.commands import AVAILABLE_COMMANDS
from ledger_app.finances.ledger import Ledger
from ledger_app.finances.monthly_financing import MonthlyReport
from ledger_app.auth.user import User
import console_utility.commands as cmds

class Engine:

    def __init__(self):
        self.app = AppData()

    def run(self):
        while True:
            pass


if __name__=='__main__':
    engine = Engine()
    engine.run()
    