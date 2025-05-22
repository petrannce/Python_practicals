import plotly.express as px

country = input("Enter your country: ")
data = {
    'country': [ country ],
    'values' : [ 100 ]
}

fig = px.choropleth(
    data,
    locations='country',
    locationmode='country names',
    color='values',
    color_continuous_scale=px.colors.sequential.Plasma,
    title=f'Choropleth Map of {country}',
    labels={'values': 'Value'},
    projection='natural earth',
    scope='world',
    hover_name='country',
    hover_data=['values']
)

fig.show()