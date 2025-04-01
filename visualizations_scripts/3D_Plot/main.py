import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x3d = np.linspace(-5, 5, 100)
y3d = np.linspace(-5, 5, 100)

X3D, Y3D = np.meshgrid(x3d, y3d)
Z3D = np.sin(np.sqrt(X3D**2 + Y3D**2))

ax.plot_surface(X3D, Y3D, Z3D, cmap='viridis', edgecolor='none')
ax.set_title('3D Surface Plot')

plt.show()