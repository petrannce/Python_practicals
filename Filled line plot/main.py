import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.fill_between(x, y, alpha=0.5, color='lightblue')
plt.show()