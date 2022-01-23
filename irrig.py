import random
import time

def plant(plant_type):
    global water_threshold


    if plant_type == "corriander":
        water_threshold = 90
        print('found corriander')

    elif plant_type == "ocimum basilicum":
        water_threshold = 90
        print('found basil')

    elif plant_type == "salvia rosmarinus":
        water_threshold = 100

        print('found salvia')

    elif plant_type == "thymus vulgaris":
        water_threshold = 90
        print('found thyme')

    else:
        # water_threshold is too low to turn stuff on
        water_threshold = 0

    print('water threshold = {th}'.format(th=water_threshold))
    return water_threshold


def soilMoisture(water_threshold):
    reading = random.uniform(50.0, 100.0)
    print('moisture sensor is {moist}'.format(moist=reading))
    if reading < water_threshold:
        print('pumps are on')
        time.sleep(5)
    else:
        print('pumps are off')