import matplotlib.pyplot as plt

categories = ['A', 'B', 'C']
values1 = [10, 15, 12]
values2 = [8, 17, 14]

plt.plot(categories, values1, marker='o', label='2023')
plt.plot(categories, values2, marker='o', label='2024')

plt.title('Slope Graph')
plt.show()