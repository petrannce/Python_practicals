import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hexbin(x, y, gridsize=50, cmap='Blues',edgecolors='grey')
plt.colorbar(label='Count in bin')

plt.title('Honeycomb pattern Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show ()
# This code generates a honeycomb pattern plot using hexagonal binning in matplotlib.