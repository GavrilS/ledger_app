"""
Commands to get finance data for analysis from users in the console.
"""
import ledger_app.finances.ledger as ledger
import ledger_app.finances.monthly_financing as mf

class FinCommands:

    def __init__(self, app_data):
        self.app_data = app_data

    def build_user_ledger(self):
        user_mail = input('Enter the user email for the ledger owner: ')
        for user in self.app_data.users:
            if user.email == user_mail:
                user_ledger = ledger.Ledger(user)
                self.app_data.add_user_ledger(user, user_ledger)
                return
            
        raise Exception('No such user was found! Try again...')

    def show_ledger(self):
        self.app_data.show_user_ledger()

    def build_monthly_finance_report(self):
        try:
            if not self.app_data.verify_active_user_ledger():
                return False

            year, month = self._get_report_period()
            data = mf.MonthlyReport(year=year, month=month)
            self.add_monthly_income(monthly_report=data, initial_report=True)
            self.add_monthly_expenditure(monthly_report=data, initial_report=True)
            print('Monthly Report: ', data)
            self.app_data.ledgers[self.app_data.active_user].finances.append(data)
            print('Monthly report added!')
        except Exception as e:
            retry = input(f"There was an issue building the monthly finance report: {e} \nDo you want to try again?[Yes/no]: ")
            if retry.lower() == 'yes':
                self.build_monthly_finance_report()

    def add_monthly_income(self, monthly_report=None, initial_report=False):
        print('Add monthly income sources in the format "Source": "Value" on separate lines.')
        print('Example:\nJob: 1800.00\nRent: 1600.00')
        print('To finish adding income data, type: done')

        if not initial_report:
            year, month = self._get_report_period()
            monthly_report = self.app_data.get_user_monthly_report(year, month) # ToDo modify the month variable to match a standard
        
        if not monthly_report:
            print('No valid report was found for this operation...')
            return False
        
        self._handle_user_input('add_income', monthly_report)

    def remove_monthly_income(self, monthly_report=None, initial_report=False):
        print('Remove monthly income sources in the format "Source": "Value" on separate lines.')
        print('Example:\nJob: 1800.00\nRent: 1600.00')
        print('To finish removing income data, type: done')

        if not initial_report:
            year, month = self._get_report_period()
            monthly_report = self.app_data.get_user_monthly_report(year, month) # ToDo modify the month variable to match a standard
        
        if not monthly_report:
            print('No valid report was found for this operation...')
            return False

        self._handle_user_input('remove_income', monthly_report)

    def add_monthly_expenditure(self, monthly_report=None, initial_report=False):
        print('Add monthly expenditure in the format "Source": "Value" on separate lines.')
        print('Example:\nBills: 300.00\nGroceries: 700.00')
        print('To finish adding expenditure data, type: done')

        if not initial_report:
            year, month = self._get_report_period()
            monthly_report = self.app_data.get_user_monthly_report(year, month) # ToDo modify the month variable to match a standard
        
        if not monthly_report:
            print('No valid report was found for this operation...')
            return False
        
        self._handle_user_input('add_expenditure', monthly_report)

    def remove_monthly_expenditure(self, monthly_report=None, initial_report=False):
        print('Remove monthly expenditure in the format "Source": "Value" on separate lines.')
        print('Example:\nBills: 300.00\nGroceries: 700.00')
        print('To finish removing expenditure data, type: done')

        if not initial_report:
            year, month = self._get_report_period()
            monthly_report = self.app_data.get_user_monthly_report(year, month) # ToDo modify the month variable to match a standard
        
        if not monthly_report:
            print('No valid report was found for this operation...')
            return False
        
        self._handle_user_input('remove_expenditure', monthly_report)

    def _handle_user_input(self, operation, monthly_report):
        try:
            data = {}
            flag = True
            while flag:
                try:
                    user_input = input().split(': ')
                    if user_input[0].lower() in 'done/exit/quit':
                        break
                    user_input_type = user_input[0]
                    value = float(user_input[1])
                    if operation == 'add_income':
                        monthly_report.add_income(source=user_input_type, value=value)
                    elif operation == 'remove_income':
                        monthly_report.remove_income(source=user_input_type, value=value)
                    elif operation == 'add_expenditure':
                        monthly_report.add_expenditure(source=user_input_type, value=value)
                    else:
                        monthly_report.remove_expenditure(source=user_input_type, value=value)
                except Exception as e:
                    print(e)
                    print('Invalid input. Try again...')
                    continue
            
        except Exception as e:
            print(e)
            print(f"Couldn't complete operation - {operation}")

    def _get_report_period(self):
        year = int(input('Provide a year for the report card: '))
        month = input('Provide a month for the report card: ')

        return year, month