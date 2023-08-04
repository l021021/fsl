import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate some random data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create two line plots
fig, ax = plt.subplots()
line1, = ax.plot(x, y1, color='blue')
line2, = ax.plot(x, y2, color='red')

# Define the update function
def update(frame):
    # Generate new data for each frame
    x = np.linspace(0, 2*np.pi, 100)
    y1 = np.sin(x + frame/10)
    y2 = np.cos(x + frame/10)
    # Update the data for the line objects
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    # Return the line objects
    return line1, line2

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()