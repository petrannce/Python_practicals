import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10)
y = np.random.randint(1, 10, size=len(x))

plt.step(x, y, color='magnenta')
plt.title('Step Plot Example')
plt.show()