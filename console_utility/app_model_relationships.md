# BASIC MODELS:

Ledger model:
- user
- finance_history => list of monthly reports
* get_monthly_income(year, month)
* get_monthly_expenditures(year, month)
* get_yearly_income_breakdown(year)
* get_yearly_expenditures_breakdown(year)

MonthlyReport model:
- year
- month
- income_sources = dict(income_src: value)
- expenditures = dict(expend_source: value)
* add_income(source, value)
* remove_income(source, value)
* show_incomes()
* add_expenditure(source, value)
* remove_expenditure(source, value)
* show_expenditures()

User model:
- name
- password
- email

COMMANDS:

AppData model:
- users = list of available users
- ledgers = dict(user_mail: ledger)
- active_user = the currently active user running commands
* set_active_user(user)
* add_user(user)
* add_user_ledger(user, ledger)
* remove_user(user)
* get_user_by_mail(user_mail) – is it needed?
* list_user_mails() - helper
* verify_active_user_ledger() - helper
* verify_active_user() - helper
* get_user_monthly_report(year, month)

FinCommands model:
* build_user_ledger() - > asks for user_email as input and builds a ledger for the user if not exists # Done
* build_monthly_finance_report() - > asks for year, month, incomes and expenditures and adds it to the active user if exists; can retry on error # Done
* add_monthly_income() - > takes user input data in the format source: value until stopped and updates the app_data in place # Done
* remove_monthly_income() - > takes user input data in the format source: value until stopped and updates the app_data in place # Done
* add_monthly_expenditure() - > takes user input data in the format source: value until stopped and updates the app_data in place # Done
* remove_monthly_expenditure() - > takes user input data in the format source: value until stopped and updates the app_data in place # Done

UserCommands model:
- create_user() - > running the command will ask the user for the relevant user data
- delete_user() -> removes a user based on specified user email

Commands constant data:
** AVAILABLE_COMMANDS = dict(command: help value)
** MONTH_DATA = dict(user_input: full month name)
* verify_year_input(year) - > make sure the user is providing valid year data


# RELATIONSHIPS:

1. Basic models:
Ledger <-> User: 1 to 1 relationship

Ledger <<<-> MonthlyReports: 1 to many - 1 ledger can have multiple monthly reports, but 1 monthly report can have only one ledger

2. Command models:
AppData <<<-> user: 1 app data to many users
AppData <<<-> ledger: 1 app data to many ledgers
FisCommands <-> AppData: 1 to 1 relationship
UserCommands <-> AppData: 1 to 1 relationship


# Functionality:
1. Engine - the runner starts the console application and keeps on waiting for commands until the user terminates the utility; at the beginning it creates the 'AppData' object that will hold the temp data generated during execution

2. Commands:
(a) User commands:
    - create user - gets input from the user to create a new user and adds it to the AppData; if this is the first user set it as the active user in the AppData model #ToDo

(b) Finance commands:
    - build user ledger - need to modify this to create a user for the currently active user if non exists #ToDo
    - build monthly finance report - should work as explained above; no more updates needed
    - add/remove monthly income - should be updated to take month/year as user input and modify the monthly reports for the active user as specified by the user input #ToDo
    - add/remove montly expenditures - should be updated to take month/year as user input and modify the montly reports for the active user as specified by the user input #ToDo