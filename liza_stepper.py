import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class motor(object):

    def __init__(self, pins):
        self.control_pins = pins
        self.currentX = 'X1'
        self.currentY = 'Y1'
        self.delay = 0.001
        self.steps_per_rev = 512
        self.sequence = [
            [1,0,0,0]
            [1,1,0,0]
            [0,1,0,0]
            [0,1,1,0]
            [0,0,1,0]
            [0,0,1,1]
            [0,0,0,1]
            [1,0,0,1]
        ]

        for pin in pins :
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)



# this function takes pins and rotation direction as an argument and makes a motor with specified pins to rotate in this direction
# it also takes time as a variable; motion will be executed for set number of seconds, depending on the axis we are moving on

    def Step(self, clockwise, t):

        pins = self.control_pins

        # motion will be performed for t seconds
        t_end = time.time() + t
        while time.time() < t_end:

            # default state of the pins is the one that gives clockwise rotation
            if clockwise == True:
                for i in range(self.steps_per_rev):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(self.control_pins[pin], self.sequence[halfstep][pin])
                    time.sleep(0.001)

            else:
                # if rotation is counterclockwise, pins are reversed
                pins = pins.reverse()
                for i in range(self.steps_per_rev):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(self.control_pins[pin], self.sequence[halfstep][pin])
                    time.sleep(0.001)



# ---------------------------------------------------------------------------------------------------------------
# Xt/Yt correspond to the time that motor should be on to get to a different X/Y position (in seconds)
Xt = 15
Yt = 20


pins1 = [4,17,27,22]
pins2 = [6, 13, 19, 26]
pins3 = [12,16,20,21]
pins4 = [18,23,24,25]

motor1 = motor(pins1)
motor2 = motor(pins2)
motor3 = motor(pins3)
motor4 = motor(pins4)

while True :
    motor1.forwardStep()
    motor2.forwardStep()
    motor3.forwardStep()
    motor4.forwardStep()
    time.sleep(1)

# LOGIC FOR STEPPER MOTORS

# ---------------------------------------------------------------------------------------------------------------
# here i assume that motor1 is used for X-axis movement and motors 2 and 3 are used for counterclockwise movement

def getToX1(currentX):
    if currentX == 'X1':
        pass
    else:
        motor1.Step(clockwise = True, Xt)
        self.currentX = 'X1'

def getToX2(currentX):
    if currentX == 'X2':
        pass
    else:
        motor1.Step(clockwise = False, Xt)
        self.currentX = 'X2'


def getToY1(currentY):
    if currentY == 'Y1':
        pass
    else:
        motor2.Step(clockwise = True, Yt)
        motor3.Step(clockwise=True, Yt)
        self.currentY = 'Y1'

def getToY2(currentY):
    if currentY == 'Y2':
        pass
    else:
        motor2.Step(clockwise=False,Yt)
        motor3.Step(clockwise=False, Yt)
        self.currentY = 'Y2'

# ---------------------------------------------------------------------------------------------------------------

def box1():
    currentX = self.currentX
    currentY = self.currentY
    getToX1(currentX)
    getToY1(currentY)

def box2():
    currentX = self.currentX
    currentY = self.currentY
    getToX2(currentX)
    getToY1(currentY)

def box3():
    currentX = self.currentX
    currentY = self.currentY
    getToX1(currentX)
    getToY2(currentY)

def box3():
    currentX = self.currentX
    currentY = self.currentY
    getToX2(currentX)
    getToY2(currentY)

# -------------------------------------------------------------------------------------------------------------
