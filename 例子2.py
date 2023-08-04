import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n=10
# Generate some random data
x = np.random.rand(n, 100)
y = np.random.rand(n, 100)


# Create n line and scatter plots
fig, ax = plt.subplots()
scats = []
lines = []
for i in range(n):
    scat = ax.scatter([], [], color='#%06x' % (int(np.random.rand()*0xffffff)))
    scats.append(scat)
    line, = ax.plot([], [], color='#%06x' % (int(np.random.rand()*0xffffff)))
    lines.append(line)

# Define the update function
def update(frame):
    # Generate new data for each frame
    x = np.random.rand(n, 100)
    y = np.random.rand(n, 100)
    # Update the positions of the scatter objects
    for i in range(n):
        scats[i].set_offsets(np.column_stack((x[i], y[i])))
        lines[i].set_data(x[i], y[i])
    # Return the line and scatter objects
    return tuple(lines + scats)

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()