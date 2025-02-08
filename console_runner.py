from console_utility.finance_commands import FinanceCommands
from console_utility.user_commands import UserCommands
from console_utility.app_data import AppData
from ledger_app.finances.ledger import Ledger
from ledger_app.finances.monthly_financing import MonthlyReport
from ledger_app.auth.user import User

class Engine:

    def __init__(self):
        self.app = AppData()

    
    