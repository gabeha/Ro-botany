
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

class motor(object):

    def __init__(self, pins):
        self.control_pins = pins
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


    def forwardStep(self):
        for i in range(self.steps_per_rev) :
            for halfstep in range(8) :
                for pin in range(4) :
                    GPIO.output(self.control_pins[pin], self.sequence[halfstep][pin])
            time.sleep(0.001)


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





    
