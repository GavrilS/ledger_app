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
        data = {}
        flag = True
        print('Add monthly income sources in the format "Source": "Value" on separate lines.')
        print('Example:\nJob: 1800.00\nRent: 1600.00\n')
        print('To finish adding income data type: done')
        while flag:
            try:
                income = input().split(': ')
                if income.lower() == 'done':
                    break
                income_type = income[0]
                value = float(income[1])
            except Exception as e:
                print('Invalid input. Try again...')
                continue
            data[income_type] = value
        
        return data

    def remove_monthly_income(self):
        pass
    
    def add_monthly_expenditure(self):
        pass

    def remove_monthly_expenditure(self):
        pass