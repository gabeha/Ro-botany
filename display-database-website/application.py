from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error
import datetime
import time
import numpy as np


app = Flask(__name__)

def getData():
    times = []
    hums =[]
    temps =[]


    db_file = '/home/pi/Documents/Sensor_Database/DHT_data.db'


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
        
        time = cr_date
        hum = float(row[1])
        temp = float(row[2])

    data = np.array([times,hums,temps])
    data = np.transpose(data)

    return data, time, hum, temp

@app.route("/")
def index():

    data, time, hum, temp = getData()

    return render_template("index.html", data = data, time = time, hum = hum, temp = temp)


if __name__ == "__main__":
   app.run(host='127.0.0.1', port=5000, debug=False)