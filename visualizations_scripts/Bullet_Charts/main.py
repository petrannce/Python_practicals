import matplotlib.pyplot as plt

categories = ['Category']
values = [80] 
ranges = [(50, 100)]  # Define the range for the bullet chart
markers = [95]

fig, ax = plt.subplots()
ax.barh(categories, values, color='lightblue')

# Plot the ranges
for i, (low, high) in enumerate(ranges):
    ax.plot([low, high], [i]*2, color='black')
    ax.plot([markers[i]], [i], marker='o', color='red', markersize=10)

plt.title('Bullet Chart')
plt.show()