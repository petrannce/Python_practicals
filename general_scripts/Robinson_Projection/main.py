import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Robinson()})
ax.coastlines()

plt.title('Robinson Projection', fontsize=16)
plt.grid(False)
plt.show()
