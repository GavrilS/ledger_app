"""
This is a model for the income/expenditures for a person in a month.
"""

class FinanceCard:

    def __init__(self, year, month):
        self._year = year
        self._month = month
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
            self.income.get(source) += value

    def remove_income(self, source, value):
        if self.income.get(source, None):
            self.income.get(source) -= value
            if self.income.get(source) <= 0:
                del self.income.get(source)

    def show_incomes(self):
        print(f"Income for {self.month} {self.year}")
        for k, v in self.income.items():
            print(f" {k}: {v}")

    @property
    def expenditures(self):
        return self._expenditures

    def add_expenditure(self, source, value):
        if not self.expenditures.get(source, None):
            self.expenditures[source] = value
        else:
            self.expenditures.get(source) += value
    
    def remove_expenditure(self, source, value):
        if self.expenditures.get(source, None):
            self.expenditures.get(source) -= value
            if self.expenditures.get(source) <= 0:
                del self.expenditures.get(source)
    
    def show_expenditures(self):
        print(f"Expenditures for {self.month} {self.year}")
        for k, v in self.expenditures.items():
            print(f" {k}: {v}")