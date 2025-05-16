import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

location_name = input("Enter a location name: ")

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:

    latitude = location.latitude
    longitude = location.longitude

    # Create a map centered at the location
    map_location = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a marker for the location
    folium.Marker([latitude, longitude], popup=location_name).add_to(map_location)

    # Save the map to an HTML file
    map_location.save("map.html")

    # Display the map in Jupyter Notebook
    display(HTML("map.html"))

else:
    print("Location not found. Please try again.")
# Note: This code requires the folium and geopy libraries.