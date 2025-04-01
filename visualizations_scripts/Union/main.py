import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# This script creates a union of two circles using GeoPandas and Shapely, and visualizes the result.

circle1 = Point(0,0).buffer(1)
circle2 = Point(0.5,0).buffer(1)

gdf = gpd.GeoDataFrame(geometry=[circle1.union(circle2)])

gdf.plot(color='blue', alpha=0.5, edgecolor='black')
plt.title('Union of Two Circles')
plt.show()