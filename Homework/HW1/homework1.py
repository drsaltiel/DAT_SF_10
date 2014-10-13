'''
Code for Homework 1 of General Assembly Data Science class
'''

import json
import datetime as dt
import sqlite3

data = []
with open('ga_hw_logins.json') as f:
    for line in f:
        data.append(json.loads(line))

date_data = []
for login in data[0]:
	date_object = dt.datetime.strptime(login, '%Y-%m-%d  %X')
    date_data.append(date_object)



# conn = sqlite3.connect('hw1.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE logins
#              (year INTEGER, month INTEGER, day INTEGER, hour INTEGER)''')
# for login in date_data:
#     c.execute("INSERT INTO logins(year,month,day,hour) VALUES (?,?,?,?)",
#     	(login.year,login.month,login.day,login.hour))

# c.execute('''SELECT  year, month, day, hour, COUNT(*) AS count
#     FROM logins GROUP BY year, month, day, hour''')

# c.execute("SELECT * FROM logins WHERE count == MAX(count)")

# conn.commit()
# conn.close()