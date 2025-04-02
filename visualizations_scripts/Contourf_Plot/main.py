import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
X, Y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))

# Define the function to plot
Z = np.sin(X**2 + Y**2)

# Plot the contourf plot
plt.contourf(X, Y, Z, cmap='coolwarm')
plt.colorbar()
plt.show()