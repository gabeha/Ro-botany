# TIMELOOP SOLUTION
# can a nesting .py file for our control circuit code
# issues:
# 1) waits for the set interval to run the program for the first time
# --> resolved by calling for the lampOn() before any looping starts, nt crucial for fans and pumps
# 2) MIGHT NOT WORK ON RASPBERRY PI --> MULTITHREADING IS WEIRD




import time
from timeloop import Timeloop
import numpy as np

from datetime import datetime, timedelta
from mockirrigation import mainIrrig, AIout

# to install timeloop on windows run in control terminal
# py -m pip install git+https://github.com/sankalpjonn/timeloop.git

# Linux/Raspberry Pi:
# python3 pip install git+https://github.com/sankalpjonn/timeloop.git


fanTime = 10 #s econds On

tl = Timeloop()
# lampCount corresponds to three different phases:
# case 0: lamp switches on for 8 hours
# case 1: lamp stays on for another 8 hours
# case 2: lamp turns off
# allows to only check on lamp every eight hours

lampCount = 0


def lampOn():
    print('lmpOn')

def lampOff():
    print('lmpOff')

def fanOn():
    print('fanOn')

def fanOff():
    print('fanOff')


# lamp must be 16 hours(seconds in testing phase) on, 8 hours/seconds off
@tl.job(interval=timedelta(seconds=8))
def lamp():
    global lampCount

    # if it's the first phase, lamp turns on for the next 8 hours
    if lampCount == 0:
        print('turning lamp on')
        lampOn()
        lampCount += 1
    elif lampCount == 1:
        print("lamp should stay on for 8 more hours")
        lampCount += 1
        pass
    else:
        print('turning lamp off')
        lampCount = 0
        lampOff()





# fan must be on for 10 seconds, off for 10 minutes
@tl.job(interval=timedelta(seconds=10))
def fans():
    print('executing fan function')
    fanOn()
    time.sleep(fanTime)
    fanOff()

# how to handle everything else?
# every 60 seconds re-initiate the irrigation cycle
# checks all four boxes and activates pumps where needed for 5 seconds
@tl.job(interval = timedelta(seconds=60))
def irrigation():
    print('irrigating')
    global plant_box

    plant_box = AIout()
    mainIrrig(plant_box)






def main():
    global lampCount, plant_box
    # block=True handles graceful shutdown of the threads
    lampOn()
    # get the AI output
    plant_box = AIout()
    mainIrrig(plant_box)
    lampCount = 2 # since timeloop will wait for the entire interval (8 hours for lamp) to start with the looping
    tl.start(block=True)

main()
