"""
Commands to get finance data for analysis from users in the console.
"""
import ledger_app.finances.ledger as ledger
import ledger_app.finances.monthly_financing as mf

def build_user_ledger(self, app_data):
    user_mail = input('Enter the user email for the ledger owner: ')
    for user in app_data.users:
        if user.email == user_mail:
            user_ledger = ledger.Ledger(user)
            app_data.add_user_ledger(user, user_ledger)
            return
        
    raise Exception('No such user was found! Try again...')

def build_monthly_finance_report(self, app_data):
    year = int(input('Provide a year for the report card: '))
    month = input('Provide a month for the report card: ')
    income = add_monthly_income()
    expenditures = add_monthly_expenditure()

    data = mf.MonthlyReport(year=year, month=month)
    for k, v in income.items():
        data.add_income(source=k, value=v)
    for k, v in expenditures.items():
        data.add_expenditure(source=k, value=v)
    
    app_data.verify_active_user()
    app_data.verify_active_user_ledger()
    
    app_data.ledgers[app_data.active_user].finances = data


def add_monthly_income(self, app_data):
    print('Add monthly income sources in the format "Source": "Value" on separate lines.')
    print('Example:\nJob: 1800.00\nRent: 1600.00')
    print('To finish adding income data, type: done')
    
    return self._handle_user_input(app_data)

def remove_monthly_income(self, app_data):
    print('Remove monthly income sources in the format "Source": "Value" on separate lines.')
    print('Example:\nJob: 1800.00\nRent: 1600.00')
    print('To finish removing income data, type: done')

    return self._handle_user_input(app_data)

def add_monthly_expenditure(self, app_data):
    print('Add monthly expenditure in the format "Source": "Value" on separate lines.')
    print('Example:\nBills: 300.00\nGroceries: 700.00')
    print('To finish adding expenditure data, type: done')
    
    return self._handle_user_input(app_data)

def remove_monthly_expenditure(self, app_data):
    print('Remove monthly expenditure in the format "Source": "Value" on separate lines.')
    print('Example:\nBills: 300.00\nGroceries: 700.00')
    print('To finish removing expenditure data, type: done')
    
    return self._handle_user_input(app_data)

def _handle_user_input(self, app_data):
    data = {}
    flag = True
    while flag:
        try:
            user_input = input().split(': ')
            if user_input.lower() == 'done':
                break
            user_input_type = user_input[0]
            value = float(user_input[1])
        except Exception as e:
            print('Invalid input. Try again...')
            continue
        data[user_input_type] = value
    
    return data