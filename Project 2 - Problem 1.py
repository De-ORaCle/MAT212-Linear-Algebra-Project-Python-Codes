'''

The code first imports the necessary libraries, including Matplotlib and Numpy. It then defines the vectors v1, v2, and v3 in R3 using Numpy arrays.

Next, the code creates a 3D plot using the plt.figure() function and the projection='3d' argument to specify a 3D projection. It then plots the vectors using the ax.quiver() function, which takes the starting point (0, 0, 0) and the x, y, and z components of each vector as arguments. The colors and labels for each vector are also specified.

The limits of the plot are then set using the ax.set_xlim(), ax.set_ylim(), and ax.set_zlim() functions. Labels for the x, y, and z axes are added using ax.set_xlabel(), ax.set_ylabel(), and ax.set_zlabel(), respectively. Finally, a legend is added using plt.legend().

The resulting 3D plot shows the three vectors v1, v2, and v3 in R3, with the x, y, and z axes labeled and the legend indicating the colors and labels for each vector.

'''


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the vectors v1, v2, and v3 in R3
v1 = np.array([1, 2, 3])
v2 = np.array([2, 3, 1])
v3 = np.array([3, 1, 2])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', label='v2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', label='v3')

# Set the limits of the plot
ax.set_xlim([-1, 4])
ax.set_ylim([-1, 4])
ax.set_zlim([-1, 4])

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()

# Show the plot
plt.show()
