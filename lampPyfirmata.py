from pyfirmata import Arduino
from time import sleep

# define the digital pins of the relay switch
PIN_LAMP = 22

if __name__ == '__main__':
    # upper USB port of Raspberry Pi is '/dev/ttyACM1', lower - '/dev/ttyACM0'
    board = pyfirmata.Arduino('/dev/ttyACM0')

    # set the pin(s) of the relay switch to the output
    lamp_pin = board.get_pin('d:PIN_LAMP:o')


def lampON():
    lamp_pin.write(1.0)

def lampOff():
    lamp_pin.write(0)


# ensure that lampPyfirmata listens to the website commands


