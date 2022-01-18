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
            if clockwise:
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

# X axis motors
motor1 = motor(pins1)
motor2 = motor(pins2)

# Y axis motors
motor3 = motor(pins3)
motor4 = motor(pins4)



# LOGIC FOR STEPPER MOTORS

# ---------------------------------------------------------------------------------------------------------------
# here i assume that motor1 is used for X-axis movement and motors 2 and 3 are used for counterclockwise movement

def getToX1(self):
    currentX = self.currentX
    if currentX == 'X1':
        pass
    else:
        motor1.Step(clockwise=True, Xt)
        motor1.currentX = 'X1'
        motor2.currentX = 'X1'


def getToX2(self):
    currentX = self.currentX
    if currentX == 'X2':
        pass
    else:
        motor1.Step(clockwise=False, Xt)
        motor1.currentX = 'X2'
        motor2.currentX = 'X2'


def getToY1(self):
    currentY = self.currentY
    if currentY == 'Y1':
        pass
    else:
        motor4.Step(clockwise=True, Yt)
        motor3.Step(clockwise=True, Yt)
        motor4.currentY = 'Y1'
        motor3.currentY = 'Y1'


def getToY2(self):
    currentY = self.currentY
    if currentY == 'Y2':
        pass
    else:
        motor4.Step(clockwise=False, Yt)
        motor3.Step(clockwise=False, Yt)
        motor4.currentY = 'Y2'
        motor3.currentY = 'Y2'


# ---------------------------------------------------------------------------------------------------------------

def box1():
    motor1.getToX1(self)
    motor3.getToY1(self)


def box2():
    motor1.getToX2(self)
    motor3.getToY1(self)


def box3():
    motor1.getToX1(self)
    motor3.getToY2(self)


def box4():
    motor1.getToX2(self)
    motor3.getToY2(self)


# ---------------------------------------------------------------------------------------------------------------

while True :
    box1()
    time.sleep(1)


# -------------------------------------------------------------------------------------------------------------
