import sqlite3
import time
import datetime

conn = sqlite3.connect('employees.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS person(clock_num TEXT, first_name TEXT, last_name TEXT, seniority_date INT, benefit_date INT, birthday INT, area TEXT)")
'''
def data_entry():
	c.execute("INSERT INTO 
	conn.commit()
	c.close()
	conn.close()
'''
@sql_entry
def make_record():
    person = {
        'clock_num': input('Clock number: \n'),
        'first_name': input('First name: \n'),
        'last_name': input('Last name: \n'),
        'seniority_date': date_name('seniority date'),
        'benefit_date': date_name('benefit date'),
        'birthday' : date_name('birthday')
        'area': input('Area: \n'),
        }

def sql_entry(func):
	def function_wrapper(X):
		func(X)
		c.execute("INSERT INTO person VALUES(clock_num, first_name, last_name, seniority_date, benefit_date, birthday, area)")
		conn.commit()
		c.close()
		conn.close()
		return 'Connected, uploaded, closed'
	return function_wrapper

create_table()

    # Decorator for date inputs, probably could put in another file and import
    # along side the 'people' class/function
    
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
