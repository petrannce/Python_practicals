import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Add the watermark
ax.text(0.5, 0.5, 'Watermark Text', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.3,
        ha='center', va='center', rotation=30)

# Show the plot
plt.show()