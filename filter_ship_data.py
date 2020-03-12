# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:26:31 2020
@author: pengrui
"""

import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta
def numSplit(num):

    hour=int(math.floor(num))
    minn = round((num-hour),2)
    mins= int(minn*60)
    time = '{0}:{1}:00'.format(str(hour).zfill(2),str(mins).zfill(2))
    return time

### set the data range of date
start_time = datetime(2017,1,1).strftime('%m-%d-%Y') 
end_time = datetime(2019,8,14).strftime('%m-%d-%Y')   # create a forder named by 'IOError'

### filter the data
'''
ship= pd.read_csv('original_ship_data.csv',skiprows= 4370000)#,nrows=200,usecols=[0,2,3,4,5,6,7,8],header=None)#totally 4710692 rows
ship.to_csv('ship_data.csv')
'''
ship= pd.read_csv('ship_data.csv',usecols=[2,3,4,5,6,7,8,9],header=None)

ship.columns=['vessel_num','dive_num','date','time','lat','lon','depth','temp']

for i in range(len(ship)):
    ship['time'][i] = numSplit(ship['time'][i])

ship['datetime']=pd.to_datetime(ship['date']+' '+ship['time'])
Time = ship['datetime']
ship['lon']=-ship['lon']
ship=ship[['vessel_num','dive_num','datetime','lat','lon','depth','temp']]
indx=np.where((Time>=start_time) & (Time<=end_time))[0]
time=Time[indx]
#time.sort()
Data = ship.ix[time.index]
Data.sort_values(by=["vessel_num","dive_num",'depth'])
Data.to_csv('filtered_ship_data.csv')
