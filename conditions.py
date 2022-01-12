import time
import pyfirmata

pumpPin1 = none
pumpPin2 = none
counter = 0
# plant type generated from AI
plant = "plant type"
# variable that stores required moister level of specified plant
water_threshold = 200
#variable for watering time, delay 35ms, uses about 70ML water, can be specific to plant
watering_time = 0.035

if __name__=='__main__':
  board = pyfirmata.Arduino('/dev/ttyACM0')
  print("it doesnt work")
  it = pyfirmata.util.Iterator(board)
  it.start()
  #pumps
  pin3 = board.get_pin('d:3:p')
  pin5 = board.get_pin('d:5:p')
  pin6 = board.get_pin('d:6:p')
  pin9 = board.get_pin('d:9:p')
  pin10 = board.get_pin('d:10:p')
  pin11 = board.get_pin('d:11:p')
  #moisture sensor
  pin_in = board.get_pin('a:0:i')
  pin = board.get_pin('d:12:o')


# sets the conditions and specific pumps to use according to plant identified
if plant == "corriander":
    water_threshold = 200
    watering_time = 0.035
    pumpPin1 = pin3
    pumpPin2 = pin5
if plant == "dill":
    water_threshold = 200
    watering_time = 0.035
    pumpPin1 = pin6
    pumpPin2 = pin9
if plant == "ocimum basilicum":
    water_threshold = 200
    watering_time = 0.035
    pumpPin1 = pin10
    pumpPin2 = pin11
if plant == "oregano":
    water_threshold = 200
    watering_time = 0.035
if plant == "salvia officinalis":
    water_threshold = 200
    watering_time = 0.035
if plant == "salvia rosmarinus":
    water_threshold = 200
    watering_time = 0.035
if plant == "spearmint":
    water_threshold = 200
    watering_time = 0.035
if plant == "thymus vulgaris":
    water_threshold = 200
    watering_time = 0.035
else:
    print("plant type not found")

#checks soil moisture and waters plants accordingly
def soil_moisture():
    global water_count
    i = 0
    # loop to sample soil moisture 50 times
    while i <= 50:
        pin.write(1.0)
        moist += pin_in.read()
        i += 1

    moist = moist / 50
    #moist = 100-(moist/1023*100)
    #percentage = map(moist, map_low, map_high, 0, 100)
    #print("Moisture Percentage:\n" + str(percentage) + "%")
    print("Moisture:\n" + str(moist))
    # compares moisture to specific threshold of plant
    if moist <= water_threshold:
        water_count += 1
        # water count == 5 to wait for water to get through pot
        if water_count == 5:
            pumps(pumpPin1, pumpPin2)
            water_count = 0

def pumps(Pin1, Pin2):
    Pin1.write(1.0)
    Pin2.write(1.0)
    time.sleep(watering_time)
    Pin1.write(0)
    Pin2.write(0)
    print("watering complete")

while True:
    # check moisture once a minute
    soil_moisture()
    time.sleep(60)

    #check moisture once a minute
    #if counter == 1:
     #soil_moisture()
    # 10 seconds
    #time.sleep(10)
    #counter += 1

    #if counter >= 6:
        #counter = 0

    #soil_moisture()





