import numpy as np
import matplotlib.pyplot as plt

random_data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(random_data, bins=30, color='blue', alpha=0.7, edgecolor='black')

plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()