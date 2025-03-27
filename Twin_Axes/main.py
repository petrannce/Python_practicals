import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax1.plot(x, np.sin(x), 'g-')
ax2.plot(x, np.cos(x), 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Sin', color='g')

ax2.set_ylabel('Cos', color='b')
plt.title('Twin Axes Example')

plt.show()