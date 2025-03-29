import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('iris')
sns.violinplot(data=data)

plt.show()