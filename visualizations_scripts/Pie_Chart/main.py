import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart')
plt.show()