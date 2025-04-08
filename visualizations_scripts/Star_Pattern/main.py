import matplotlib.pyplot as plt
import numpy as np

rows, cols = 5, 5

x = np.arange(cols)
y = np.arange(rows)
X,y = np.meshgrid(x, y)

X = X.flatten()
Y = y.flatten()
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(X, Y, marker='*', s=300, c='gold', edgecolors='black')

ax.set_xlim(-1, cols)
ax.set_ylim(-1, rows)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

ax.set_aspect('equal')
plt.title("Star Pattern")
plt.show()