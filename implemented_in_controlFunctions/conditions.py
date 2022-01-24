import time
import pyfirmata

pumpPin1 = none
pumpPin2 = none
lamp_counter = 1
moisture_counter = 1
fan_counter = 1

global map_low
global map_high
global plant_box[3]
global plant_position

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

  pin4 = board.get_pin('d:4:p')
  pin7 = board.get_pin('d:7:p')
  #light
  pin8 = board.get_pin('d:8:p')
  pin13 = board.get_pin('d:13:p')

  #fan
  pin12 = board.get_pin('d:12:p')
  pin14 = board.get_pin('d:14:p')


  #moisture sensor
  pin_in = board.get_pin('a:0:i')
  pin = board.get_pin('d:12:o')


# sets the conditions and specific pumps to use according to plant identified
def plant(plant_type):
  # variable that stores required moister level of specified plant
  global water_threshold
  # variable for watering time, delay 35ms, uses about 70ML water, can be specific to plant
  global watering_time

  if plant_type == "corriander":
     water_threshold = 90
     watering_time = 0.035
     pumpPin1 = pin3
     pumpPin2 = pin5
     map_low = 200
     map_high = 800
     plant_position = plant_box[0]

  if plant_type == "ocimum basilicum":
     water_threshold = 100
     watering_time = 0.035
     pumpPin1 = pin10
     pumpPin2 = pin11
     map_low = 200
     map_high = 800
     plant_position = plant_box[1]

  if plant_type == "salvia rosmarinus":
     water_threshold = 100
     watering_time = 0.035
     pumpPin1 = pin6
     pumpPin2 = pin9
     map_low = 200
     map_high = 800
     plant_position = plant_box[2]

  if plant_type == "thymus vulgaris":
     water_threshold = 80
     watering_time = 0.035
     pumpPin1 = pin4
     pumpPin2 = pin7
     map_low = 200
     map_high = 800
     plant_position = plant_box[3]

  if plant_type == "dill":
     print("plant type: dill is not currently present in plant box")

  if plant_type == "spearmint":
     print("plant type: spearmint is not currently present in plant box")

  if plant_type == "salvia officinalis":
     print("plant type: salvia officinalis is not currently present in plant box")

  if plant_type == "oregano":
     print("plant type: oregano is not currently present in plant box")

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
    print("Moisture:\n" + str(moist))

    moisture_percentage = map(moist, map_low, map_high, 0, 100)
    print("Moisture Percentage:\n" + str(percentage) + "%")

    # compares moisture to specific threshold of plant
    if moisture_percentage <= water_threshold:
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

#switch light on for 8 hours and off for 8 hours
def lamp_on():
    pin8.write(1.0)
    pin13.write(1.0)

def lamp_off():
    pin8.write(0)
    pin13.write(0)

def fan_on():
    pin12.write(1.0)
    pin14.write(1.0)
    time.sleep(15)
    pin12.write(0)
    pin14.write(0)


def map(x, in_min, in_max, out_min, out_max):
    return ((x-in_min) * (out_max - out_min)/(in_max - in_min) + out_min)


def moisture_reader():
    if moisture_counter == 1:
        soil_moisture()
        # 10 seconds
        time.sleep(10)
        moisture_counter += 1

    if moisture_counter >= 7:
        counter = 1
        soil_moisture()


identify
each
plant
y = 0
while y <= 3:
    # move camera to all first position
    # identify plant in first position
    plant = plant_box[y]

def conditions_box0 ():
    plant(plant_box[0])
    soil_moisture()

def conditions_box0 ():
    plant(plant_box[0])
    soil_moisture()

def conditions_box1 ():
    plant(plant_box[1])
    soil_moisture()

def conditions_box2 ():
    plant(plant_box[2])
    soil_moisture()

def conditions_box3 ():
    plant(plant_box[3])
    soil_moisture()

#plant
#type()
#soil_moisture()
#identify each plant
#for 1 to 4

#conditions()

#plant type ()
#soil_moisture()


while True:

    conditions_box0()
    conditions_box1()
    conditions_box2()
    conditions_box3()
    #plant("corriander")
    #soil_moisture()
    #time.sleep(60)

    #switch on lamp every 8 hours + check moisture once a minute

    if lamp_counter & fan_counter == 1:
        lamp_on()
        fan_on()
        # 10 seconds
        time.sleep(10)
        lamp_counter += 1



    if fan_counter >= 60:
       fan_on()
       fan_counter = 1




    if lamp_counter >= 5760.1:
        while x <= 2880:
          lamp_off()
          x =+ 1
        lamp_counter = 1







