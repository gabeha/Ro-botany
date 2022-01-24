# Stepper1.py
# I don't know which libraries will be used to move stepper
# >> adjust accordingly 

#import RPi.GPIO as GPIO

import pyfirmata
import time


#X_A1 = 30  # adapt to your wiring
#X_A2 = 32 # ditto
#X_B1 = 33 # ditto
#X_B2 = 13 # ditto

#Y_A1 = 8  # adapt to your wiring
#Y_A2 = 10 # ditto
#Y_B1 = 11 # ditto
#Y_B2 = 13 # ditto

delay = 0.005 # time to settle

#def setupX():
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(X_A1, GPIO.OUT)
    #GPIO.setup(X_A2, GPIO.OUT)
    #GPIO.setup(X_B1, GPIO.OUT)
    #GPIO.setup(X_B2, GPIO.OUT)


def setupX():
    X_A1 = board.get_pin('d:22:p')
    X_A2 = board.get_pin('d:24:p')
    X_B1 = board.get_pin('d:26:p')
    X_B2 = board.get_pin('d:28:p')
    X_C1 = board.get_pin('d:30:p')
    X_C2 = board.get_pin('d:32:p')
    X_D1 = board.get_pin('d:34:p')
    X_D2 = board.get_pin('d:36:p')

def setupY():
    Y_A1 = board.get_pin('d:38:p')
    Y_A2 = board.get_pin('d:40:p')
    Y_B1 = board.get_pin('d:42:p')
    Y_B2 = board.get_pin('d:44:p')
    Y_C1 = board.get_pin('d:46:p')
    Y_C2 = board.get_pin('d:48:p')
    Y_D1 = board.get_pin('d:50:p')
    Y_D2 = board.get_pin('d:52:p')


#def setupY():
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(Y_A1, GPIO.OUT)
    #GPIO.setup(Y_A2, GPIO.OUT)
    #GPIO.setup(Y_B1, GPIO.OUT)
    #GPIO.setup(Y_B2, GPIO.OUT)

def forwardStepX():
    setStepperX(1, 0, 1, 0)
    setStepperX(0, 1, 1, 0)
    setStepperX(0, 1, 0, 1)
    setStepperX(1, 0, 0, 1)

def backwardStepX():
    setStepperX(1, 0, 0, 1)
    setStepperX(0, 1, 0, 1)
    setStepperX(0, 1, 1, 0)
    setStepperX(1, 0, 1, 0)
  
#def setStepperX(in1, in2, in3, in4):
    #GPIO.output(X_A1, in1)
    #GPIO.output(X_A2, in2)
    #GPIO.output(X_B1, in3)
    #GPIO.output(X_B2, in4)
    #time.sleep(delay)

def setStepperX(in1, in2, in3, in4):
    X_A1.write(in1)
    X_A2.write(in2)
    X_B1.write(in3)
    X_B2.write(in4)
    X_C1.write(in1)
    X_C2.write(in2)
    X_D1.write(in3)
    X_D2.write(in4)
    time.sleep(delay)

def forwardStepY():
    setStepperY(1, 0, 1, 0)
    setStepperY(0, 1, 1, 0)
    setStepperY(0, 1, 0, 1)
    setStepperY(1, 0, 0, 1)

def backwardStepY():
    setStepperY(1, 0, 0, 1)
    setStepperY(0, 1, 0, 1)
    setStepperY(0, 1, 1, 0)
    setStepperY(1, 0, 1, 0)
  
#def setStepperY(in1, in2, in3, in4):
    #GPIO.output(Y_A1, in1)
    #GPIO.output(Y_A2, in2)
    #GPIO.output(Y_B1, in3)
    #GPIO.output(Y_B2, in4)
    #time.sleep(delay)


def setStepperY(in1, in2, in3, in4):
    Y_A1.write(in1)
    Y_A2.write(in2)
    Y_B1.write(in3)
    Y_B2.write(in4)
    Y_C1.write(in1)
    Y_C2.write(in2)
    Y_D1.write(in3)
    Y_D2.write(in4)
    time.sleep(delay)

x_tot = 1000  # total length of movement defined in camera steps
y_tot = 1000  # total length of movement defined in camera steps

# coordinates = [(x,y) for x in range( x_tot) for y in range( y_tot )]
p_def = [x_tot / 2, y_tot / 2]  # default position (middle)
p1 = [x_tot / 4, y_tot / 4]  # plant1 : bottom-left
p2 = [(x_tot - x_tot / 4), y_tot / 4]  # plant2 : bottom-right
p3 = [x_tot / 4, (y_tot - y_tot / 4)]  # plant3 : top-left
p4 = [(x_tot - x_tot / 4), (y_tot - y_tot / 4)]  # plant4 : top-right

p_prev = p_def  # GLOBAL variable to save previous position

if __name__=='__main__':
  board = pyfirmata.Arduino('/dev/ttyACM0')
  print("it doesnt work")
  it = pyfirmata.util.Iterator(board)
  it.start()

setupX()  # setup motor for x coordinate movement
setupY()  # setup motor for y coordinate movement


# moves camera from current position to target position
def move_to(p_target):
    x_d = p_target[1] - p_prev[1]
    y_d = p_target[2] - p_prev[2]

    # move in x direction
    if x_d < 0:
        for i in reversed(range(x_d)):
            backwardStepX()
    if x_d > 0:
        for i in (range(x_d)):
            forwardStepX()

    # move in y direction
    if y_d < 0:
        for i in reversed(range(y_d)):
            backwardStepY()
    if y_d > 0:
        for i in (range(y_d)):
            forwardStepY()

    # set endpoint as current point for later movement
    global p_prev
    p_prev = p_target


# move to default position from initial
def initialize():
    global p_prev
    p_prev = [0, 0]  # fill x_init and y_init according to cam position at setup
    move_to(p_def)  # move to default position


# returns to default position
def return_to_def():
    move_to(p_def)


# moves to selected plant based on input
def plant_move(plant_select):
    if plant_select == 1:
        move_to(p1)
    if plant_select == 2:
        move_to(p2)
    if plant_select == 3:
        move_to(p3)
    if plant_select == 4:
        move_to(p4)
