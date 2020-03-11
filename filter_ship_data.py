# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:26:31 2020

@author: pengrui
"""

import pandas as pd
import numpy as np

###filter the data
ship= pd.read_csv('nefsc_hydro_for_erddap.csv',skiprows= 4370000)#,nrows=200,usecols=[0,2,3,4,5,6,7,8],header=None)
ship.to_csv('ship_data.csv')

ship= pd.read_csv('ship_data.csv',usecols=[2,3,4,5,6,7,8,9],header=None)

ship.columns=['vessel_num','dive_num','date','time','lat','lon','depth','temp']

for i in range(len(ship)):
    ship['time'][i] = numSplit(ship['time'][i])

ship['datetime']=pd.to_datetime(ship['date']+' '+ship['time'])
ship['lon']=-ship['lon']
ship=ship[['vessel_num','dive_num','datetime','lat','lon','depth','temp']]

#ship.to_csv('ship_data.csv')
