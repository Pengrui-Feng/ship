import pandas as pd
import numpy as np
import math
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from turtleModule import draw_basemap


###observe the positon of ship
lonsize = [-77.8, -63.8]#tu99
latsize = [32.8, 46.8]#tu199
obsdata = pd.read_csv('ship_data.csv')
lon=obsdata['lon']
lat=obsdata['lat']
fig =plt.figure()
ax = fig.add_subplot(111)
for i in range(10000,len(obsdata),100):
    plt.scatter(lon[i],lat[i],s=15,linewidths=None)
draw_basemap(fig, ax, lonsize, latsize, interval_lon=2, interval_lat=2) 

plt.show()
