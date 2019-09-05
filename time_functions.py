import datetime
from datetime import date, time, datetime, timedelta
from time import ctime, strftime, struct_time, strptime, localtime, mktime, time

class tm_func:

    def __init__(self, datetimer, date_name, time_since):
        self.datetimer = datetimer
        self.date_name = date_name
        self.time_since = time_since

    def datetimer(func):
        # Decorator - Turns user input into datetime.date object.
        def function_wrapper(X):
            print('Enter the ', X, 'in \n YYYY, MM, DD format.')
            func(X)
            date_entry = input(': ')
            year, month, day = map(int, date_entry.split(', '))
            return date(year, month, day)
        return function_wrapper

    @datetimer
    def date_name(*X):
        # Used to create the datetime object for initial input into db.
        pass

    def time_since():
        today = date.today()
        birthday = tm_func.date_name('birthday')
        t = today.strftime('%j')
        x = birthday.strftime('%j')
        # If the birthday hasn't happened in current year then years would be 1 too high
        if int(x) > int(t):
            diff = (today.toordinal() - 365) - birthday.toordinal()
            since = date.timetuple(diff.fromordinal())
            return "You are {} years and {} months old.".format(since.tm_year, since.tm_mon)
        else:
            diff = (today.toordinal()) - birthday.toordinal()
            since = date.timetuple(diff.fromordinal())
            return "You are {} years and {} months old.".format(since.tm_year, since.tm_mon)
