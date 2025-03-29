import numpy as np
import matplotlib.pyplot as plt

X,Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.contour(X, Y, Z, cmap='viridis')
plt.show()