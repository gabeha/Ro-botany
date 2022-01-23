import time
import os
from irrig import plant, soilMoisture

def AIout():
    # reads out what plnts are in what positions
    global plant_box
    plant_box = [None, None, None, None]
    if os.path.isfile('AIout.txt'):
        f = open('AIout.txt', 'r')
        for i in range(4):
            plant_box[i] = f.readline().strip('\n')
        f.close()
        print("AI found plants, they are {plants}".format(plants=plant_box))
    else:
        # there is no AI output, no plants are in the box
        print('AI didnt find any plants')

    return plant_box


# function that will maintain irrigation in all 4 boxes
def mainIrrig(plant_box):
    for box in plant_box:
        print(box)
        if str(box) == 'None':
            print('box is None')

        else:
            print('box is not None')
            # calls function that establishes watering threshold for plant
            water_threshold = plant(box)
            soilMoisture(water_threshold)






