import plotly.express as px

data = {
    'Country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'],
    'values': [100, 200, 150, 300, 250],
}
fig = px.choropleth(data_frame=data,
                    locations='Country',
                    locationmode='country names',
                    color='values',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Choropleth Map Example',
                    labels={'values': 'Value'},
                    projection='natural earth')
fig.show()