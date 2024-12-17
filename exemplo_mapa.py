import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Generate some random temperature data for demonstration
np.random.seed(0)
latitudes = np.random.uniform(-90, 90, 100)
longitudes = np.random.uniform(-180, 180, 100)
temperatures = np.random.uniform(-10, 30, 100)

# Create a Basemap instance
m = Basemap(projection='cyl', resolution='l', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)

# Create a figure and axis
plt.figure(figsize=(10, 6))
ax = plt.gca()

# Draw coastlines, countries, and states
m.drawcoastlines()
m.drawcountries()
m.drawstates()

# Convert latitude and longitude to x and y using the map projection
x, y = m(longitudes, latitudes)

# Scatter plot with temperature as color
sc = m.scatter(x, y, c=temperatures, cmap='coolwarm', s=50, edgecolors='k', linewidths=1, zorder=10)

# Add a colorbar
cbar = plt.colorbar(sc, orientation='vertical')
cbar.set_label('Temperature (°C)')

# Set plot title and show the plot
plt.title('Temperature Map')
plt.show()
