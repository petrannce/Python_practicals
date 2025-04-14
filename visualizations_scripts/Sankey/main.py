import plotly.graph_objects as go

# Define the labels for the nodes in the Sankey diagram
labels = ["Source A", "Source B", "Source C", "Target X", "Target Y", "Target Z"]

# Define the source and target indices for the links
source = [0, 1, 0, 2, 3, 3, 4]
target = [3, 3, 4, 4, 5, 5, 5]
values = [8, 4, 2, 8, 4, 2, 3]

# Create a Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color="blue"
    ),
    link=dict(
        source=source,
        target=target,
        value=values
    )
)])

# Update layout
fig.update_layout(title_text="Sankey Diagram Example", font_size=10)
fig.show()
# This code creates a simple Sankey diagram using Plotly. The diagram represents the flow of values from sources to targets.