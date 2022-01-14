
import pyfirmata
import time

class motor(object):

    def __init__(self):
        
        self.A1 = board.get_pin('d:3:p')
        self.A2 = board.get_pin('d:5:p')
        self.B1 = board.get_pin('d:6:p')
        self.B2 = board.get_pin('d:9:p')

    def setStepper(self, in1, in2, in3, in4):
        self.A1.write(in1)
        self.A2.write(in2)
        self.B1.write(in3)
        self.B2.write(in4)

    def forwardStep(self):
        self.setStepper(1, 0, 1, 0)
        self.setStepper(0, 1, 1, 0)
        self.setStepper(0, 1, 0, 1)
        self.setStepper(1, 0, 0, 1)

    def backwardStep(self):
        self.setStepper(1, 0, 0, 1)
        self.setStepper(0, 1, 0, 1)
        self.setStepper(0, 1, 1, 0)
        self.setStepper(1, 0, 1, 0)


if __name__=='__main__':
  board = pyfirmata.Arduino('/dev/ttyACM0')
  print("it doesnt work")
  it = pyfirmata.util.Iterator(board)
  it.start()

motor1 = motor()  # setup motor for x coordinate movement

for i in range(10):
    motor1.forwardStep()
