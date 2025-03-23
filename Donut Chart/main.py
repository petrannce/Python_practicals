import matplotlib.pyplot as plt

sizes = [30, 20, 50]
labels = ['A', 'B', 'C']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', 
        wedgeprops = {'width': 0.3})
plt.show()