import numpy as np
import matplotlib.pyplot as plt

size = 10

x = np.arange(size)
y = np.where(x % 2 == 0, 1, 0)

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(x, y, marker='o', markersize=8, color='orange', linestyle='-', linewidth=2)

ax.set_xlim(-1, size)
ax.set_ylim(-0.5, 1.5)

ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

ax.set_title('ZigZag Pattern Plot', fontsize=16, fontweight='bold')
plt.show()