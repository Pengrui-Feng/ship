# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:42:22 2019
plot and display ptt-date
@author: pengrui
"""
import matplotlib.dates as dt
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd

#db= 'tu73' #tu73,tu74,tu94,tu98,tu99,tu102
path1='/content/drive/My Drive/ship_Summary.csv'
path2='/content/drive/My Drive/'

df = pd.read_csv(path1)
ptt = df['vessel_num']
tracks=df['length_of_track']
start = df['start_date']
end = df['end_date']

fig =plt.figure()
for i in df.index:
    s = datetime.strptime(start[i], '%Y-%m-%d %H:%M:%S').date()
    e = datetime.strptime(end[i], '%Y-%m-%d %H:%M:%S').date()
    ss = dt.date2num(s)
    ee = dt.date2num(e)
    plt.plot([ss,ee],[i,i], marker = ".")
    a=tracks[i].find(' ')
    #plt.text(ss,i+0.1,tracks[i][0:a+5],size=9)
ax = plt.gca()
formatter = dt.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.grid(True)
ax.yaxis.grid(True)
firstdays=dt.MonthLocator() # Get data for the first day of the month
locate=dt.MonthLocator(range(1, 13), bymonthday=1, interval=6) # Get data on the first day of every 3 months

ax.xaxis.set_major_locator(locate) # Set the main scale
ax.xaxis.set_minor_locator(firstdays) # Set minor scale

fig.autofmt_xdate() # Auto rotate xlabel  
plt.tick_params(axis='y', which='both', labelright='on') # 
#tu73,tu74,tu94,tu98,tu99,tu102
plt.yticks([-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],['EY1501','GU1401','GU1402','GU1506','GU1608','GU1701','GU1706','GU1804','HB1401','HB1403','HB1405','HB1501','HB1502','HB1503','HB1505','HB1506','HB1601','HB1603','HB1604','HB1701','HB1702','HB1802','HB1803','HB1804','HB1805','HB1806','PC1405','PC1607','PC1609','PC1706','S11401','S11402','S11501','S11601','S11701','S11801','S11802'])

plt.title('ship_duration')
plt.savefig(path2+'ship_duration.png',dpi=200)
plt.show()

