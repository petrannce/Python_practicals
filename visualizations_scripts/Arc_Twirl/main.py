import numpy as np
import matplotlib.pyplot as plt

# Arc Twirl Visualization
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# Create a twirling arc pattern
num_arcs = 100
angle_step = np.pi / 10
radius_step = 0.01

# Create arcs with increasing radius and rotation
for i in range(num_arcs):
    theta = np.linspace(0, np.pi, 50)
    r = i * radius_step
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    angle = i * angle_step
    x_rot = x * np.cos(angle) - y * np.sin(angle)
    y_rot = x * np.sin(angle) + y * np.cos(angle)

    ax.plot(x_rot, y_rot, color=plt.cm.viridis(i / num_arcs), lw=2)

plt.title('Arc Twirl Pattern', fontsize=14)
plt.show()