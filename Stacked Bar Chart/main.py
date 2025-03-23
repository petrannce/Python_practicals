import matplotlib.pyplot as plt

bar1 = [3, 4, 5]
bar2 = [6, 7, 8]

x_labels = ['A', 'B', 'C']

plt.bar(x_labels, bar1, label='Bar 1')
plt.bar(x_labels, bar2, bottom=bar1, label='Bar 2')

plt.legend()
plt.show()
