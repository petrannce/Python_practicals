import matplotlib.pyplot as plt
import numpy as np

categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [25, 30, 15, 10, 20]

colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))
plt.bar(categories, values, color=colors)
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Coloured Bar Graph of Fruits')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()