import sqlite3
from sqlite3 import Error
import datetime
import numpy as np

times = []
hums =[]
temps =[]
counter = 0


db_file = '/home/gabe/Documents/Code/Re-Do/DHT_data.db'


conn = None
try:
    conn = sqlite3.connect(db_file)
except Error as e:
    print(e)

cur = conn.cursor()
cur.execute("SELECT * FROM DHT_data")

rows = cur.fetchall()

for row in rows:
    cr_date = row[0]
    cr_date = datetime.datetime.strptime(cr_date, '%Y-%m-%d %H:%M:%S')
    cr_date = cr_date.strftime("%H%M%S")

    times.append(cr_date)
    hums.append(float(row[1]))
    temps.append(float(row[2]))
    counter +=1


data = np.array([times,hums,temps])
print(data.shape)




