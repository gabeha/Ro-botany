import sqlite3 as lite
import Adafruit_DHT
from pyfirmata import Arduino, util
from time import sleep



# sleep time
fs=1

# ----------------------------------------
# PINS
DHT_PIN = 4   # GPIO4
ArduinoPins = 4 # A0, A1, A2, A3

board = Arduino('/dev/ttyUSB0')
# ----------------------------------------

con = lite.connect('/home/pi/Documents/Sensor_Database/DHT_data.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS DHT_data")
    # add four additional columns for the moisture sensor data
    cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, hum NUMERIC, temp NUMERIC, moist1 NUMERIC, moist2 NUMERIC,\
    moist3 NUMERIC, moist4 NUMERIC,)")


def read_DHTdata():
    DHT_SENSOR = Adafruit_DHT.DHT22
    
    hum, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    moist = readMoist()
    if hum is not None and temp is not None:
        hum = round(hum, 2)
        temp = round(temp, 2)
        insert_data(hum, temp, moist)


    
def insert_data(hum, temp, moist):
    cur.execute("INSERT INTO DHT_data values(datetime('now'),?,?)", (hum,temp))
    for i in range(ArduinoPins):
        cur.execute("INSERT INTO DHT_data values(?)", moist[i])
    con.commit()

def readMoist():
    it = util.Iterator(board)
    it.start()
    moist = []
    for i in range(ArduinoPins):
        board.analog[i].enable_reporting()
        moist[i] = board.analog[i].read()

    return moist



def main():
    
    while True:
        read_DHTdata()
#         for row in cur.execute("SELECT * FROM DHT_data"):
#             print (row)
        sleep(fs)

main()
    
    
