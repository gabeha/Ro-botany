import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# ---------------------------------------------------------------------------------------------------------------
# Xt/Yt correspond to the time that motor should be on to get to a different X/Y position (in seconds)
Xt = 5
Yt = 5




# X axis motors

motor1 = [4,17,27,22]
motor2 = [6, 13, 19, 26]

# Y axis motors

motor3 = [12,16,20,21]
motor4 = [18,23,24,25]


pins_all = [4,17,27,22, 6, 13, 19, 26, 12,16,20,21, 18,23,24,25]
pins = []
global currentX, currentY
currentX = 'X1'
currentY = 'Y1'

delay = 0.001
steps_per_rev = 512
forward = 0

sequence = [
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]
]

for pin in pins_all :
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)



# this function takes pins and rotation direction as an argument and makes a motor with specified pins to rotate in this direction
# it also takes time as a variable; motion will be executed for set number of seconds, depending on the axis we are moving on

def Step(motor1, motor2, clockwise):
    if clockwise:
        print('rotating clockwise')
        for i in range(512):
            for halfstep in range(8):
                for pin in range(4):

                    GPIO.output(motor1[pin], sequence[halfstep][pin])
                    GPIO.output(motor2[pin], sequence[halfstep][pin])
                time.sleep(0.001)

    else:
        print('rotating anticlockwise')
                # if rotation is counterclockwise, pins are reversed
            #motor = motor[::-1]
        for i in range(512):
            for halfstep in range(8):
                for pin in range(3,-1,-1):
                    GPIO.output(motor1[pin], sequence[halfstep][pin])
                    GPIO.output(motor2[pin], sequence[halfstep][pin])
                time.sleep(0.001)



# LOGIC FOR STEPPER MOTORS

# ---------------------------------------------------------------------------------------------------------------
# here i assume that motor1 is used for X-axis movement and motors 2 and 3 are used for counterclockwise movement

def getToX1(currentX):
    
    print(currentX)
    if currentX == 'X1':
        pass
    else:
        x_end = Xt 
        for i in range(int(x_end)):
            # simultaneous clockwise rotation moves camera from X1 to X2
            Step(motor1, motor2, True)
        currentX = 'X1'
    return currentX


def getToX2(currentX):
    
    if currentX == 'X2':
        pass
    else:
        x_end = Xt 
        for i in range(int(x_end)):
            # simultaneous anticlockwise rotation moves camera from X2 to X1
            Step(motor1, motor2, False)
        currentX = 'X2'
    return currentX


def getToY1(currentY):
    if currentY == 'Y1':
        pass
    else:
        x_end = Xt 
        for i in range(int(x_end)):
            # simultaneous clockwise rotation moves camera from Y1 to Y2
            Step(motor3, motor4, True)
        currentX = 'Y1'
    return currentY    


def getToY2(currentY):
    if currentY == 'Y2':
        pass
    else:
        x_end = Xt 
        for i in range(int(x_end)):
            # simultaneous anticlockwise rotation moves camera from Y2 to Y1
            Step(motor3, motor4, False)
        currentX = 'Y2'
    return currentY


# ---------------------------------------------------------------------------------------------------------------

def box1():
    print('started box1')
    currentx = getToX1(currentX)
    currentx = getToY1(currentY)
    print('finished box1')
    return currentx, currentx


def box2():
    currentx = getToX2(currentX)
    currenty = getToY1(currentY)
    return currentx, currenty


def box3():
    currentx = getToX1(currentX)
    currenty = getToY2(currentY)
    return currentx, currenty


def box4():
    currentx = getToX2(currentX)
    currenty = getToY2(currentY)
    return currentx, currenty


# ---------------------------------------------------------------------------------------------------------------

while True :
  
  Step(motor3, motor4, True)  



# -------------------------------------------------------------------------------------------------------------


