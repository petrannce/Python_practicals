import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)
ax.plot(x, np.exp(x))
ax2.plot(x, np.exp(x))

ax2.set_ylim(0, 5)

plt.subplots_adjust(hspace=0.05)
plt.show()
# The code creates a figure with two subplots, one above the other, sharing the same x-axis.