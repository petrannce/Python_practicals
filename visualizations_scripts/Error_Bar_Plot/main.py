import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)
y = 2 * x + 2
y_errors = np.random.rand(len(x)) * 2
colors = plt.cm.plasma(np.linspace(0, 1, len(x)))

plt.figure()
for i in range(len(x)):
    plt.errorbar(
        x[i], y[i], yerr=y_errors[i], fmt='*', capsize=5, color=colors[i], label=f'Point {i+1}',
        markersize=8, elinewidth=2
        )
    
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Error Bar Plot with Coloured Points')
plt.legend()
plt.show()