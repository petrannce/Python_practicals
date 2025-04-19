import plotly.express as px

data = {
    'country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'],
    'latitude': [37.0902, 56.1304, 23.6345, -14.2350, -38.4161],
    'longitude': [-95.7129, -106.3468, -102.5528, -51.9253, -63.6167],
    'population': [329.409, 38.565, 126.566, 210.980, 45.733]
}

fig = px.scatter_geo(
    data, 
    
    lat="latitude", 
    lon="longitude", 
    size="population", 
    color="country", 
    hover_name="country",
    title="Population of Countries in the Americas",
)
fig.show()