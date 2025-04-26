import matplotlib.pyplot as plt

categories = ['category 1', 'category 2', 'category 3', 'category 4']
values = [80, 20, 50, 30]

fig, ax1 = plt.subplots()
ax1.bar(categories, values, color='blue')
ax1.set_ylabel('Values', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

ax2 = ax1.twinx()
cumulative_values = [sum(values[:i+1]) for i in range(len(values))]
ax2.plot(categories, cumulative_values, color='red', marker='o')
ax2.set_ylabel('Cumulative Values', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Pareto Chart')
plt.show()
# This code creates a Pareto chart using matplotlib. It displays a bar chart for the values of different categories and a line chart for the cumulative values.