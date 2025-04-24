import plotly.graph_objects as go

stages = [ 'A', 'B', 'C', 'D' ]
values = [ 1000, 700, 400, 250 ]

fig = go.Figure(go.Funnel(
    y=stages,
    x=values,
    textinfo="value+percent initial+percent previous",
))

fig.update_layout(
    title_text="Funnel Chart Example",
    title_x=0.5,
)

fig.show()
# fig.write_image("funnel_chart.png")  # Uncomment to save the figure as an image