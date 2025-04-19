import numpy as np
import matplotlib.pyplot as plt

times = np.arange(0, 100, 1)
values = np.cumsum(np.random.randn(100))

plt.plot(times, values)
plt.title('Cumulative Sum of Random Values')
plt.show()