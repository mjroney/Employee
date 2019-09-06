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

    def time_since(X):
        today = date.today()
        X = tm_func.date_name(X)
        t = today.strftime('%j')
        x = X.strftime('%j')
        # '-1' puts result as completed years, not 'completed plus current'
        diff = (today.toordinal()) - X.toordinal()
        since = date.timetuple(date.fromordinal(diff))
        return "You are {} years and {} months old.".format(since.tm_year - 1, since.tm_mon)
