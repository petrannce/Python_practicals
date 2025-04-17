import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

coordinates = [
    (0, 0), (0, 50), (30, 50), (30, 0), (0, 0)
]
parcel = Polygon(coordinates)
gdf = gpd.GeoDataFrame({'geometry': [parcel]})
gdf.plot(facecolor='lightblue', edgecolor='blue')

plt.title('Land Parcel Plot')
plt.show()