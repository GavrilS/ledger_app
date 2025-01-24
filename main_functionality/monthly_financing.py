"""
This is a model for the income/spenditures for a person in a month.
"""

class MonthlyFinancing:

    def __init__(self, year, month):
        self._year = year
        self._month = month
        self._income_sources = {}
        self._spenditures = {}

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
    
    @property
    def income(self):
        return self._income_sources

    @month.setter
    def month(self, value):
        if not value:
            raise Exception('The Month needs to be specified.')
        
        self._month = value
    
    def add_income(source, value):
        if not self.income.get(source, None):
            self.income[source] = value
        else:
            self.income.get(source) += value

    def remove_income(source, value):
        if self.income.get(source, None):
            self.income.get(source) -= value
            if self.income.get(source) <= 0:
                del self.income.get(source)