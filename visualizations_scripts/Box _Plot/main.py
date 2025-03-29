import numpy as np
import matplotlib.pyplot as plt

# Random data
data = [np.random.randn(100) for _ in range(4)]
plt.boxplot(data)

# Show the plot
plt.show()