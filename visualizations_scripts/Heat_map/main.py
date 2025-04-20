import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.rand(10, 10)
sns.heatmap(data, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)

plt.show()
# This code generates a heatmap using Seaborn and Matplotlib. The data is a 10x10 matrix of random values, and the heatmap is annotated with the values formatted to two decimal places. The color map used is 'coolwarm', and a color bar is included to indicate the scale of the values.