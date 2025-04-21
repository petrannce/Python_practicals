import plotly.express as px

# Sample data
data = {
    'id': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'parent': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
    'value': [10, 15, 7, 8, 12, 6, 5, 8],
}

# Create a suburst chart
fig = px.sunburst(data, names='id', parents='parent', values='value')

# Set the chart title
fig.update_layout(title_text='Sunburst Chart')

# Show the chart
fig.show()
