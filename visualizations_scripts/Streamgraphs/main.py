import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.stackplot(x, y1, y2, baseline='wiggle', labels=['sin(x)', 'cos(x)'], colors=['#ff9999', '#66b3ff'])
plt.legend(loc='upper left')
plt.title('Streamgraph')
plt.show()