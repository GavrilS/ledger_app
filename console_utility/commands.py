"""
This file provides a list of available commands in the format of a dictionary where each key
is a command and its value is the explanation of the command.
"""

AVAILABLE_COMMANDS = {
    'create': {
        'user': 'Create a new user for the application',
        'ledger': 'Create a new ledger for the user',
        'report': 'Create a monthly report for the user'
    },
    'delete': {
        'user': 'Deletes a user based on an email'
    },
    'add': {
        'income': 'Adds income source/value for a specific monthly report card; the monthly report needs to exist already',
        'expenses': 'Adds expense source/value for a specific monthly report card, the monthly report needs to exist already'
    },
    'remove': {
        'income': 'Remove already existing income source/value for a specific monthly report card; the card needs to exist already',
        'expenses': 'Remove already existing expense source/value for a specific monthly report card; the card needs to exist already'
    },
    'show': {
        'users': 'Show a list of existing users',
        'active user': 'Shows the currently active user in the application'
    },
    'change': {
        'user': 'Changes the active user'
    }
}

MONTHS = {
    '1': 'January',
    '01': 'January',
    'january': 'January',
    'jan': 'January',
    #-----------
    '2': 'February',
    '02': 'February',
    'february': 'February',
    'feb': 'February',
    #-----------
    '3': 'March',
    '03': 'March',
    'march': 'March',
    'mar': 'March',
    #-----------
    '4': 'April',
    '04': 'April',
    'april': 'April',
    'apr': 'April',
    #-----------
    '5': 'May',
    '05': 'May',
    'may': 'May',
    #-----------
    '6': 'June',
    '06': 'June',
    'june': 'June',
    'jun': 'June',
    #-----------
    '7': 'July',
    '07': 'July',
    'july': 'July',
    'jul': 'July',
    #-----------
    '8': 'August',
    '08': 'August',
    'august': 'August',
    'aug': 'August',
    #-----------
    '9': 'September',
    '09': 'September',
    'september': 'September',
    'sep': 'September',
    #-----------
    '10': 'October',
    'october': 'October',
    'oct': 'October',
    #-----------
    '11': 'November',
    'november': 'November',
    'nov': 'November',
    #-----------
    '12': 'December',
    'december': 'December',
    'dec': 'December',
}

def command_parser(command=None):
    if not command or 'help' in command.lower():
        print('Available commands:')
        for option in AVAILABLE_COMMANDS.keys():
            print('Option: ', option)
            for cmd, description in AVAILABLE_COMMANDS[option].items():
                print(f"  {cmd}: {description}")
        print('='*80, '\n')
        return None

    cmd_components = command.split(' ')
    if len(cmd_components) < 2 or not AVAILABLE_COMMANDS.get(cmd_components[0], None) or \
        not AVAILABLE_COMMANDS[cmd_components[0]].get(cmd_components[1], None):
        command_parser()
    
    else:
        return f"{cmd_components[0]} {cmd_components[1]}"

def get_standard_month(month=None):
    if not MONTHS.get(month, None):
        month_formats = ' \njanuary\njan\n01\n1\n'
        raise Exception(f"Invalid month format provided. Months should be in one of these formats: {month_formats}")
    
    return MONTHS.get(month)