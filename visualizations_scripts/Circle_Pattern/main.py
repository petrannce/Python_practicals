import numpy as np
import matplotlib.pyplot as plt

radius = 1
num_points = 50
theta = np.linspace(0, 2 * np.pi, num_points)

x = radius * np.cos(theta)
y = radius * np.sin(theta)
fig, ax = plt.subplots()

ax.scatter(x, y, s=50, c='black')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

ax.set_aspect('equal')
ax.axis('off')
plt.title('Circle Pattern', fontsize=20, fontweight='bold')
plt.show()