import matplotlib.pyplot as plt

sizes = [30, 20, 50, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
circle = plt.Circle((0, 0), 0.70, color='white')
plt.gca().add_artist(circle)

plt.title('Donut Chart ')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()