import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.swarmplot(data=tips, x="day", y="total_bill")

plt.title("Swarm Plot of Total Bill by Day")
plt.show()
# The code creates a swarm plot using the Seaborn library, visualizing the distribution of total bills by day in the tips dataset.