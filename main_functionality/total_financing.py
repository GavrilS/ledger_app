"""
This is a model for the income/expenditures for a person as a total.
"""

ANALYSIS_TYPE_MESSAGE = {
    'yearly_income': 'Showing the income for year $year_value:',
    'yearly_expenditure': 'Showing expenditures for year $year_value:'
}

class TotalFinanceModel:

    def __init__(self, user=None, finance_history=None):
        self._user = user
        self._finance_history = finance_history

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if not value:
            raise Exception('User must be specified!')
        self._user = value
    
    @property
    def finances(self):
        return self._finance_history

    @finances.setter
    def finances(self, value):
        if not value:
            raise Exception('Missing user finances...')
        
        self._finance_history = value

    def get_monthly_income(self, year, month):
        self._get_monthly_finances_by_type(year, month, 'income')

    def get_monthly_expenditures(self, year, month):
        self._get_monthly_finances_by_type(year, month, 'expenditure')

    def _get_monthly_finances_by_type(self, year, month, finance_type='income'):
        if not year or not month:
            raise Exception('Select both an year and a month to check!')
        
        for item in self.finance_history:
            if item.month == month and item.year == year:
                if finance_type.lower() == 'income':
                    item.show_incomes()
                else:
                    item.show_expenditures()
                return
    
    def get_yearly_income_breakdown(self, year):
        yearly_data = self._extract_yearly_analysis_data(year, 'income')
        self._visualize_yearly_finance_data(yearl_data, 'yearly_income', year)

    def get_yearly_expenditures_breakdown(self, year):
        yearly_data = self._extract_yearly_analysis_data(year, 'expenditures')
        self._visualize_yearly_finance_data(yearl_data, 'yearly_expenditure', year)

    def _extract_yearly_analysis_data(self, year, analysis_type='income'):
        if not year:
            raise Exception('Provide the year for the yearly analysis!')

        yearly_data = {}
        count = 0
        for item in self.finance_history:
            if item.year == year:
                if analysis_type.lower() == 'income':
                    for k,v in item.income.items():
                        if not yearly_data.get(k, None):
                            yearly_data[k] = v
                        else:
                            yearl_data.get(k) += v
                else:
                    for k,v in item.expenditures.items():
                        if not yearly_data.get(k, None):
                            yearly_data[k] = v
                        else:
                            yearl_data.get(k) += v
                count += 1
            
            if count == 12:
                break

        return yearly_data

    def _visualize_yearly_finance_data(self, yearly_data, analysis_type='yearly_income', year):
        print(ANALYSIS_TYPE_MESSAGE.get(
            analysis_type, 'yearly_income').replace('$year_value', str(year)))

        for k, v in yearl_data.items():
            print(f" {k}: {v}")
