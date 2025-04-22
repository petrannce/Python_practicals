import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.randn(1000)
y = np.random.randn(1000)

# Create a 2D histogram
plt.hist2d(x, y, bins=(30, 30), cmap='viridis')
plt.colorbar(label='brequency')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('2D Histogram of Random Data')
plt.show()