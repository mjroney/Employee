from datetime import date, time, datetime

def datetimer(func):
    def function_wrapper(X):
        print('Enter your ', X, 'in \n YYYY, MM, DD format.')
        func(X)
        date_entry = input(': ')
        year, month, day = map(int, date_entry.split(', '))
        return date(year, month, day)
    return function_wrapper


@datetimer
def date_name(X):
    pass



# Call like:
# date_name('birthday')
