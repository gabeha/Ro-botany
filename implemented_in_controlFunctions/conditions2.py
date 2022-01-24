import time
import pyfirmata






lamp_counter = 1
moisture_counter = 1
fan_counter = 1



global plant_position

if __name__=='__main__':
  board = pyfirmata.Arduino('/dev/ttyACM0')
  print("it doesnt work")
  it = pyfirmata.util.Iterator(board)
  it.start()
  #pumps
  pin2 = board.get_pin('d:2:o')
  pin3 = board.get_pin('d:3:o')


 


  #moisture sensor
  pin_in = board.get_pin('a:1:i')
  pin = board.get_pin('d:7:o')


# sets the conditions and specific pumps to use according to plant identified
def plant(plant_type):
  # variable that stores required moister level of specified plant
  global water_threshold
  # variable for watering time, delay 35ms, uses about 70ML water, can be specific to plant
  global watering_time
  global pumpPin1 
  global pumpPin2
  global map_low
  global map_high

  if plant_type == "corriander":
     water_threshold = 90
     watering_time = 10
     pumpPin1 = pin2
     pumpPin2 = pin3
     map_low = 0.9863
     map_high = 0.150
   

  if plant_type == "ocimum basilicum":
     water_threshold = 100
     watering_time = 10
     pumpPin1 = pin10
     pumpPin2 = pin11
     map_low = 200
     map_high = 800
   

  if plant_type == "salvia rosmarinus":
     water_threshold = 100
     watering_time = 10
     pumpPin1 = pin6
     pumpPin2 = pin9
     map_low = 200
     map_high = 800
     

  if plant_type == "thymus vulgaris":
     water_threshold = 80
     watering_time = 10
     pumpPin1 = pin4
     pumpPin2 = pin7
     
     map_low = 1.0 # air dried soil: 760-800 on arduino - 0.5298 in pyfirmata, air: 1023 in arduino,
     map_high = 0.240 # FC soil: 360 on arduino - 0.24 in pyfirmata
     box[3]

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
    print('started soil moisture func')
   
    
        
    pin.write(1.0)
    while pin_in.read() == None or pin_in.read() == 0.0 :
        print('moisture value None or 0')
        pass
    moist = pin_in.read()
    print(moist)
       

    moisture_percentage = map(moist, map_low, map_high, 0, 100)
    print("Moisture Percentage:\n" + str(moisture_percentage) + "%")

    # compares moisture to specific threshold of plant
    if moisture_percentage <= water_threshold:
            print("pumps should switch on")
            print(pumpPin1, pumpPin2)
            pumps(pumpPin1, pumpPin2)
            time.sleep(5)

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

 



while True:

    #conditions_box0()
    #conditions_box1()
    #conditions_box2()
    #conditions_box3()
    plant("corriander")
    soil_moisture()
    time.sleep(60)

    #switch on lamp every 8 hours + check moisture once a minute

  


