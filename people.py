import sqlite3
import datetime
from datetime import date, time, datetime, timedelta
import time_functions

db_filename = input('Provide the database path: \n')

conn = sqlite3.connect('db_location')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS People(clock_num TEXT NOT NULL UNIQUE PRIMARY KEY, first_name TEXT, last_name TEXT, birthday INTEGER, seniority_date INTEGER, benefit_date INTEGER, area TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS License(serial_number TEXT PRIMARY KEY, issuing_state TEXT, expiration_date INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS Jobs(dumpTruck TEXT, carryAll TEXT, articulatingDumpTruck TEXT, flatbedTruck TEXT, fuelTruck TEXT, stellarShuttle TEXT, luggerRolloff TEXT, snowPlow TEXT, waterTruck TEXT, dozer TEXT, excavator TEXT, backhoe TEXT, loader TEXT, vibratoryRoller TEXT, roadGrader TEXT, forkLift TEXT, landfillGuard TEXT, carryallBackingMan TEXT, aaaExcavator TEXT, bfCarryAll TEXT, annualLechateInspection TEXT, hydrantReplacement TEXT)")

def add_person()
    clock_num = input('Clock number: \n')
    first_name = input('First name: \n')
    last_name = input('Last name: \n')
    birthday = date_name('birthday')
    seniority_date = date_name('seniority date')
    benefit_date = date_name('benefit date')
    area = input('Area: \n')
    c.execute("INSERT INTO People VALUES(?, ?, ?, ?, ?, ?)", (clock_num, first_name, last_name, birthday, seniority_date, benefit_date, area))
    conn.commit()
    c.close()
    conn.close()
    displayed = last_name + ', ' + first_name[0] + '.'
    print(displayed + ' has been entered into the database.')
    add_license()

def add_license():
    serial_number = input("What is the license's serial number? \n:  ")
    issuing_state = input('Where was the license issued \n(OH for Ohio, etc...) : ')
    expiration_date = date_name('expiration_date')
    c.execute("INSERT INTO License VALUES(?, ?, ?)", (serial_number, issuing_state, expiration_date))
    conn.commit()
    c.close()
    conn.close()

########################################
### Below here is a template, not ready.
### This is sample from sentdex (on youtube)
########################################

def read_from_db():
    c.execute('''SELECT * FROM stuffToPlot WHERE value = 9 AND keyword = 'Python' ''')
    # data = c.fetchall()
    # print(data)
    for row in c.fetchall():
        print row
#        print row[0]


def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    for row in data:
        print row
#    print len(c.fetchall())
    c.execute('UPDATE stuffToPlot SET value = 11 WHERE value = 1')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print 'After UPDATE'
    for row in data:
        print row
#    print len(c.fetchall())

    c.execute('DELETE FROM stuffToPlot WHERE value = 11')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print 'After DELETE'
    for row in data:
        print row
