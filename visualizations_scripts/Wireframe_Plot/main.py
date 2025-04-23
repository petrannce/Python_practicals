import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.linspace(-5, 5, 50)
b = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(a, b)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()
wf = plt.axes(projection='3d')
wf.plot_wireframe(X, Y, Z, color='blue', alpha=0.5)

wf.set_title('Wireframe Plot')
plt.show()