import networkx as nx
import matplotlib.pyplot as plt

G = nx.cycle_graph(20)  # Create a cycle graph with 20 nodes
pos = nx.spring_layout(G)  # positions for all nodes

nx.draw(G, pos, node_color='lightblue', 
        with_labels=True, node_size=100)

plt.title("Network Graph")
plt.show()
# fig.savefig("network_graph.png")  # Uncomment to save the figure as an image