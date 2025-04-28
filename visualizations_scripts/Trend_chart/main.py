import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

trend = np.polyfit(x, y, 1)  # Linear trend
trend_function = np.poly1d(trend) # Create a polynomial function from the coefficients

plt.plot(x, y, 'o', label='Original data')
plt.plot(x, trend_function(x), 'r--', label='Trend line')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Trend Chart')
plt.legend()
plt.show()