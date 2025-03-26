import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
# The grid of points is created using the numpy function mgrid
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2

# Plot the stream plot
plt.streamplot(X, Y, U, V)
plt.show()