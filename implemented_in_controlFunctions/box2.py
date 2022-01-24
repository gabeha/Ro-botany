import random
import time

if __name__=='__main__':
  board = pyfirmata.Arduino('/dev/ttyACM0')
  print("it doesnt work")
  it = pyfirmata.util.Iterator(board)
  it.start()
# pumps
pin3 = board.get_pin('d:3:p')
pin5 = board.get_pin('d:5:p')
pin6 = board.get_pin('d:6:p')
pin9 = board.get_pin('d:9:p')

# light
pin8 = board.get_pin('d:8:p')
pin13 = board.get_pin('d:13:p')

# fan
pin12 = board.get_pin('d:12:p')
pin14 = board.get_pin('d:14:p')

# moisture sensor
pin_in = board.get_pin('a:0:i')
moisture_sensor1 = board.get_pin('d:12:o')
pin_in = board.get_pin('a:1:i')
moisture_sensor2 = board.get_pin('d:12:o')
pin_in = board.get_pin('a:2:i')
moisture_sensor3 = board.get_pin('d:12:o')
pin_in = board.get_pin('a:3:i')
moisture_sensor4 = board.get_pin('d:12:o')

def plant(plant_type):
    global water_threshold
    global pumpPin1
    global map_low
    global map_high
    global moisture_sensor

    if plant_type == "corriander":
        water_threshold = 90
        pumpPin1 = pin3
        moisture_sensor = moisture_sensor1
        print('found corriander')

    elif plant_type == "ocimum basilicum":
        water_threshold = 90
        water_threshold = 100
        pumpPin1 = pin10
        moisture_sensor = moisture_sensor2
        print('found basil')

    elif plant_type == "salvia rosmarinus":
        water_threshold = 100
        water_threshold = 100
        pumpPin1 = pin6
        moisture_sensor = moisture_sensor3
        print('found salvia')

    elif plant_type == "thymus vulgaris":
        water_threshold = 90
        pumpPin1 = pin4
        moisture_sensor = moisture_sensor4
        print('found thyme')

    elif plant_type == "dill":
        print("plant type: dill is not currently present in plant box")

    elif plant_type == "spearmint":
        print("plant type: spearmint is not currently present in plant box")

    elif plant_type == "salvia officinalis":
        print("plant type: salvia officinalis is not currently present in plant box")

    elif plant_type == "oregano":
        print("plant type: oregano is not currently present in plant box")

    elif:
        print("plant type not found")

    else:
        # water_threshold is too low to turn stuff on
        water_threshold = 0

    print('water threshold = {th}'.format(th=water_threshold))
    return water_threshold

def pumps(Pin1):
    Pin1.write(1.0)
    time.sleep(1)
    Pin1.write(0)
    print("watering complete")


def soil_moisture(water_threshold):
    global water_count
    i = 0
    # loop to sample soil moisture 50 times
    while i <= 50:
        moisture_sensor.write(1.0)
        moist += moisture_sensor()
        i += 1

    moist = moist / 50
    print("Moisture:\n" + str(moist))

    moisture_percentage = map(moist, map_low, map_high, 0, 100)
    print("Moisture Percentage:\n" + str(moisture_percentage) + "%")

    # compares moisture to specific threshold of plant
    if moisture_percentage <= water_threshold:
            pumps(pumpPin1)
            print('pumps are on')
            time.sleep(5)
    else:
        print('pumps are off')

