import sqlite3 as lite
import sys
import Adafruit_DHT
import time

fs=1

con = lite.connect('/home/pi/Documents/Sensor_Database/DHT_data.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS DHT_data")
    cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, hum NUMERIC, temp NUMERIC)")


def read_DHTdata():
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    
    hum, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if hum is not None and temp is not None:
        hum = round(hum, 2)
        temp = round(temp, 2)
        insert_data(hum, temp)
    return hum, temp

    
def insert_data(hum, temp):
    cur.execute("INSERT INTO DHT_data values(datetime('now'),?,?)", (hum,temp))
    con.commit()
    

def main():
    
    while True:
        hum, temp = read_DHTdata()
        insert_data(hum, temp)
#         for row in cur.execute("SELECT * FROM DHT_data"):
#             print (row)
        time.sleep(fs)

main()
    
    
