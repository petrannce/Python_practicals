import numpy as np
import matplotlib.pyplot as plt

rows, cols = 10, 10
tile_size = 1

fig, ax = plt.subplots(figsize = (8, 8))
ax.set_xlim(0, cols * tile_size)
ax.set_ylim(0, rows * tile_size)
ax.set_aspect('equal')
ax.axis('off')

colors = ['#6FA3EF', '#F4C542', '#E96A64', '#9C5E7F']

for row in range(rows):
    for col in range(cols):
        x = col * tile_size
        y = row * tile_size
        color = np.random.choice(colors)
        square = plt.Rectangle((x, y), tile_size, tile_size, color=color, ec='white', lw=2)
        ax.add_patch(square)

plt.title('Mosaic Tile Pattern', fontsize=16, fontweight='bold', color='navy',pad=15)
plt.show()