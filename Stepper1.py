# Stepper1.py
# I don't know which libraries will be used to move stepper
# >> adjust accordingly 

import RPi.GPIO as GPIO
import time


X_A1 = 8  # adapt to your wiring
X_A2 = 10 # ditto
X_B1 = 11 # ditto
X_B2 = 13 # ditto

Y_A1 = 8  # adapt to your wiring
Y_A2 = 10 # ditto
Y_B1 = 11 # ditto
Y_B2 = 13 # ditto

delay = 0.005 # time to settle

def setupX():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(X_A1, GPIO.OUT)
    GPIO.setup(X_A2, GPIO.OUT)
    GPIO.setup(X_B1, GPIO.OUT)
    GPIO.setup(X_B2, GPIO.OUT)

def setupY():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Y_A1, GPIO.OUT)
    GPIO.setup(Y_A2, GPIO.OUT)
    GPIO.setup(Y_B1, GPIO.OUT)
    GPIO.setup(Y_B2, GPIO.OUT)

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
  
def setStepperX(in1, in2, in3, in4):
    GPIO.output(X_A1, in1)
    GPIO.output(X_A2, in2)
    GPIO.output(X_B1, in3)
    GPIO.output(X_B2, in4)
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
  
def setStepperY(in1, in2, in3, in4):
    GPIO.output(Y_A1, in1)
    GPIO.output(Y_A2, in2)
    GPIO.output(Y_B1, in3)
    GPIO.output(Y_B2, in4)
    time.sleep(delay)
