import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
fig, ax = plt.subplots(2, 2)

x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100)

ax[0,0].plot(x, np.sin(x))
ax[0,1].plot(x, np.cos(x))
ax[1,0].plot(x, np.tan(x))
ax[1,1].plot(x, np.exp(x))

plt.show()