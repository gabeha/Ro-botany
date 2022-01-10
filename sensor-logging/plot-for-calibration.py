import numpy as np
import serial
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    if ser.in_waiting > 1:
        # Read temperature (Celsius) from TMP102
        ser_line = ser.readline()

        # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(float(ser_line))

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Moisture over time')
        plt.ylabel('relative moisture')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
