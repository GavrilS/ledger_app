"""
This is a report for the income/expenditures for a person in a month.
"""

class MonthlyReport:

    def __init__(self, year, month):
        self.year = year
        self.month = month
        self._income_sources = {}
        self._expenditures = {}

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not value:
            raise Exception('The Year must be specified.')
        
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if not value:
            raise Exception('The Month needs to be specified.')
        
        self._month = value

    @property
    def income(self):
        return self._income_sources
    
    def add_income(self, source, value):
        if not self.income.get(source, None):
            self.income[source] = value
        else:
            self.income[source] += value

    def remove_income(self, source, value):
        if self.income.get(source, None):
            self.income[source] -= value
            if self.income.get(source) <= 0:
                del self.income[source]

    def show_incomes(self):
        print(f"Income for {self.month} {self.year}")
        for k, v in self.income.items():
            print(f" {k}: {v}")

    @property
    def total_income(self):
        total_income = 0
        for k, v in self.income.items():
            total_income += v
        
        # print(f"Total income for {self.month} {self.year} is {total_income}")
        return total_income

    @property
    def expenditures(self):
        return self._expenditures

    def add_expenditure(self, source, value):
        if not self.expenditures.get(source, None):
            self.expenditures[source] = value
        else:
            self.expenditures[source] += value
    
    def remove_expenditure(self, source, value):
        if self.expenditures.get(source, None):
            self.expenditures[source] -= value
            if self.expenditures.get(source) <= 0:
                del self.expenditures[source]
    
    def show_expenditures(self):
        print(f"Expenditures for {self.month} {self.year}")
        for k, v in self.expenditures.items():
            print(f" {k}: {v}")

    @property
    def total_expenses(self):
        total_expenses = 0
        for k, v in self.expenditures.items():
            total_expenses += v
        
        # print(f"Total expenses for {self.month} {self.year} is {total_expenses}")
        return total_expenses

    def monthly_balance(self):
        monthly_balance = self.total_income - self.total_expenses

        # print(f"Monthly balance for {self.month} {self.year} is {monthly_balance}")
        return monthly_balance

    def __str__(self):
        year = f"\n Year - {self.year}"
        month = f"\n Month - {self.month}"
        income = f"\n Income - {self.income}"
        expenses = f"\n Expenses - {self.expenditures}"
        total_income = f"\n Total income - {self.total_income}"
        total_expenses = f"\n Total expenses - {self.total_expenses}"
        monthly_balance = f"\n Monthly balance - {self.monthly_balance()}"

        return f"Monthly Report: {year}{month}{income}{expenses}{total_income}{total_expenses}{monthly_balance}"