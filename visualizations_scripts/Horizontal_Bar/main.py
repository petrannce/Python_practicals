import numpy as np
import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 15, 7, 12]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(categories, values, color='skyblue', edgecolor='black')
# Add labels and title
ax.set_xlabel('Values')
ax.set_title('Horizontal Bar Chart Example')
# Add grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()