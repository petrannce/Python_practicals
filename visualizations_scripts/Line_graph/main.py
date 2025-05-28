import matplotlib.pyplot as plt
import numpy as np

# Sample data
x_values = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y_values = np.sin(x_values)

# Create the line graph
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, color='coral', linestyle='-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph Example')

# Show the graph
plt.grid(True, linestyle='--')
plt.show()