
import pyfirmata
import time




def setupX():
    X_A1 = board.get_pin('d:3:p')
    X_A2 = board.get_pin('d:5:p')
    X_B1 = board.get_pin('d:6:p')
    X_B2 = board.get_pin('d:9:p')

def setStepperX(in1, in2, in3, in4):
    X_A1.write(in1)
    X_A2.write(in2)
    X_B1.write(in3)
    X_B2.write(in4)

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

i=0
if __name__=='__main__':
  board = pyfirmata.Arduino('/dev/ttyACM0')
  print("it doesnt work")
  it = pyfirmata.util.Iterator(board)
  it.start()

setupX()  # setup motor for x coordinate movement

while i <= 10:
    forwardStepX()
    i += 1