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
        pass

    def remove_monthly_income(self):
        pass
    
    def add_monthly_expenditure(self):
        pass

    def remove_monthly_expenditure(self):
        pass