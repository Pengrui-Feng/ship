# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:04:05 2019

@author: pengrui
"""
'''
!apt-get install libgeos-dev
!pip install https://github.com/matplotlib/basemap/archive/master.zip
!pip install pyproj==1.9.6
'''
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap
from turtleModule import draw_basemap
#from matplotlib.mlab import griddata
def draw_basemap(fig, ax, lonsize, latsize, interval_lon=2, interval_lat=2):
    ax = fig.sca(ax)
    dmap = Basemap(projection='cyl',
                   llcrnrlat=min(latsize)-0.01,
                   urcrnrlat=max(latsize)+0.01,
                   llcrnrlon=min(lonsize)-0.01,
                   urcrnrlon=max(lonsize)+0.01,
                   resolution='h',ax=ax)
    dmap.drawparallels(np.arange(int(min(latsize)),
                                 int(max(latsize))+1,interval_lat),
                       labels=[1,0,0,0], linewidth=0,fontsize=20)
    dmap.drawmeridians(np.arange(int(min(lonsize))-1,
                                 int(max(lonsize))+1,interval_lon),
                       labels=[0,0,0,1], linewidth=0,fontsize=20)
    dmap.drawcoastlines()
    dmap.fillcontinents(color='grey')
    dmap.drawmapboundary()
db= 'tu73' #tu73,tu74,tu94,tu98,tu99,tu102
path1='/content/drive/My Drive/102_ship_data.csv'
path2='/content/drive/My Drive/'

color=['g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate']
t_ids=[118940, 118941, 118944, 118947, 118948, 118951, 118943, 118945,118946, 118942, 118952, 118949, 118950, 118953, 118954, #tu_73
       118884, 118894, 118896, 118885, 118887, 118888, 118889, 118890,118886, 118891, 118893, 118892, 118899, 118901, 118903, 118897,118898, 118900, 118902, 118895, 118906, 118905, 118904, 118913, #tu74
       118905, 149443, 149448, 149449, 149445, 149446, 149447, 151557,151558, 151561, 149450, 151559, 151560,  #tu94
       159795, 159796, 159797, 161305, 161444, 161868, 161293, 161302,161441, 161443, 172178, 172180, 172184, 161442, 161445, 172193,172181, 172189, 172177, 172182, 172183, 172185, 172186, 172187,172190, 172192, 172194, 172196, #tu98
       161426, 161427, 161428, 161432, 161433, 161435, 161429, 161436,161437, 161430, 161434, 161439, 161431, 161438, 161440, #tu_99
       161291, 161292, 161296, 172191, 175934, 175935, 161295, 175939,161299, 161303, 161294, 161297, 161298, 161300, 161301, 161304,172179, 172188, 175938, 175932, 175936, 175940] #tu_102

lonsize = [-79, -69]#tu99
latsize = [35, 42]#tu199
obsdata = pd.read_csv(path1) # has both observed and modeled profiles
obstime =  pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in obsdata['datetime']))
obsLat=obsdata['lat']
obsLon=obsdata['lon']
obsturtle_id=obsdata['vessel_num']
ids=obsturtle_id.unique() # this is the interest turtle id
  
fig =plt.figure()
ax = fig.add_subplot(111)

plt.scatter(lon, lat,s=15,linewidths=None)  #  
draw_basemap(fig, ax, lonsize, latsize, interval_lon=2, interval_lat=2)    

plt.title('ship_scatterplot')#('%s profiles(%s~%s)'% (e,obsTime[0],obsTime[-1]))
plt.legend(loc='lower right',ncol=2,fontsize = 'xx-small')
plt.savefig(path2+'ship_ScatterPlot.png',dpi=200)
      
