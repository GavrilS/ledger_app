"""
Commands to get finance data for analysis from users in the console.
"""

class Commands:

    def __init__(self):
        pass

    def build_monthly_finance_model(self):
        year = int(input('Provide a year for the report card: '))
        month = input('Provide a month for the report card: ')
        income = add_monthly_income()
        expenditures = add_monthly_expenditure()
        data = {
            'year': year,
            'month': month,
            'income': income,
            'expenditures': expenditures
        }
        return data


    def add_monthly_income(self):
        print('Add monthly income sources in the format "Source": "Value" on separate lines.')
        print('Example:\nJob: 1800.00\nRent: 1600.00')
        print('To finish adding income data, type: done')
        
        return self._handle_user_input()

    def remove_monthly_income(self):
        print('Remove monthly income sources in the format "Source": "Value" on separate lines.')
        print('Example:\nJob: 1800.00\nRent: 1600.00')
        print('To finish removing income data, type: done')

        return self._handle_user_input()
    
    def add_monthly_expenditure(self):
        print('Add monthly expenditure in the format "Source": "Value" on separate lines.')
        print('Example:\nBills: 300.00\nGroceries: 700.00')
        print('To finish adding expenditure data, type: done')
        
        return self._handle_user_input()

    def remove_monthly_expenditure(self):
        print('Remove monthly expenditure in the format "Source": "Value" on separate lines.')
        print('Example:\nBills: 300.00\nGroceries: 700.00')
        print('To finish removing expenditure data, type: done')
        
        return self._handle_user_input()

    def _handle_user_input(self):
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