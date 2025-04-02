import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 300)
x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t))
y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t))
plt.figure(figsize=(6, 6))

plt.plot(x, y, color='blue', linewidth=2)
plt.plot(-x, y, color='orange', linewidth=2)

plt.title('Butterfly Pattern Plot', fontsize=14)
plt.axis('equal')
plt.axis('off')
plt.show()