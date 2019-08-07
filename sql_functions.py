def roster():
	# Checks DB and presents roster.

    cur.execute('''CREATE TABLE IF NOT EXISTS People
    (clock_num INTEGER PRIMARY KEY, first_name TEXT, \
    last_name TEXT, seniority_date INTEGER)''')
    if cur.rowcount = 0:
    	employee()
    elif cur.rowcount != 0:
    	cur.execute('SELECT * FROM People WHERE area = \
            'Mobile' ORDER BY seniority_date')
    	for row in cur:
    		print(row)
