import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randn(1000)

sns.histplot(data, kde=True)

plt.title('Histogram with KDE')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()