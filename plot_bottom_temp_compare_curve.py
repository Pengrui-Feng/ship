#@title Default title text
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:22:57 2020

@author: Administrator
"""

import matplotlib.dates as mt
from datetime import datetime,timedelta
import calendar
import pandas as pd 
import matplotlib.pylab as plt
from time import strptime,strftime



name=['year','datehour','name','date','time','apm','timedelata','lat','lon','depth','temp']
DMF1=pd.read_csv('/content/dDMF1.csv',skiprows=1,names=name)
#DMF1.dropna(axis=0, how='any', inplace=True)
for i in range(len(DMF1)):
    DMF1['date'][i]=DMF1['date'].iloc[i]+' '+DMF1['time'].iloc[i][:2]
a=pd.to_datetime(DMF1['date'])
DMF1['date']=mt.date2num(a)

d2000=DMF1[DMF1['year']==2000]
d2001=DMF1[DMF1['year']==2001]
d2002=DMF1[DMF1['year']==2002]
d2003=DMF1[DMF1['year']==2003]
d2004=DMF1[DMF1['year']==2004]
d2005=DMF1[DMF1['year']==2005]
d2006=DMF1[DMF1['year']==2006]
d2007=DMF1[DMF1['year']==2007]
d2008=DMF1[DMF1['year']==2008]
d2009=DMF1[DMF1['year']==2009]
d2010=DMF1[DMF1['year']==2010]
d2011=DMF1[DMF1['year']==2011]
d2012=DMF1[DMF1['year']==2012]
d2013=DMF1[DMF1['year']==2013]
d2014=DMF1[DMF1['year']==2014]
d2015=DMF1[DMF1['year']==2015]

colors=['g','orange','b','c','peru','lime','brown','r','y','pink','indigo','coral','plum','maroon','peachpuff','gold','chocolate']
lines=['-','--','-.',':','-','--','-.',':','-','--','-.',':','-','--','-.',':']
fig=plt.figure(figsize=(20,15))
ax1=fig.add_axes([0.1, 0.1, 0.8,0.8])
plt.plot(d2000['date']-365*0,d2000['temp'],color=colors[0],linestyle=lines[0],label=str(2000))
plt.plot(d2001['date']-365*1-1,d2001['temp'],color=colors[1],linestyle=lines[1],label=str(2001))
plt.plot(d2002['date']-365*2,d2002['temp'],color=colors[2],linestyle=lines[2],label=str(2002))
plt.plot(d2003['date']-365*3,d2003['temp'],color=colors[3],linestyle=lines[3],label=str(2003))
plt.plot(d2004['date']-365*4,d2004['temp'],color=colors[4],linestyle=lines[4],label=str(2004))
plt.plot(d2005['date']-365*5-1,d2005['temp'],color=colors[5],linestyle=lines[5],label=str(2005))
plt.plot(d2006['date']-365*6,d2006['temp'],color=colors[6],linestyle=lines[6],label=str(2006))
plt.plot(d2007['date']-365*7,d2007['temp'],color=colors[7],linestyle=lines[7],label=str(2007))
plt.plot(d2008['date']-365*8,d2008['temp'],color=colors[8],linestyle=lines[8],label=str(2008))
plt.plot(d2009['date']-365*9-1,d2009['temp'],color=colors[9],linestyle=lines[9],label=str(2009))
plt.plot(d2010['date']-365*10,d2010['temp'],color=colors[10],linestyle=lines[10],label=str(2010))
plt.plot(d2011['date']-365*11,d2011['temp'],color=colors[11],linestyle=lines[11],label=str(2011))
plt.plot(d2012['date']-365*12,d2012['temp'],color=colors[12],linestyle=lines[12],label=str(2012))
plt.plot(d2013['date']-365*13-1,d2013['temp'],color=colors[13],linestyle=lines[13],label=str(2013))
plt.plot(d2014['date']-365*14,d2014['temp'],color=colors[14],linestyle=lines[14],label=str(2014))
plt.plot(d2015['date']-365*15,d2015['temp'],color=colors[15],linestyle=lines[15],label=str(2015))


ax = plt.gca()
ax.xaxis.set_major_formatter(mt.DateFormatter('%m-%d'))
#ax.yaxis.grid(True)
firstdays=mt.MonthLocator() 
locate=mt.MonthLocator(range(1, 13), bymonthday=1, interval=2) 
ax.xaxis.set_major_locator(locate)
ax.xaxis.set_minor_locator(firstdays) 
ax.yaxis.set_major_locator(plt.MultipleLocator(2))
ax1.set_ylim(-2,20)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.rcParams['font.sans-serif'] = ['SimHei']
ax1.set_xlabel('时间',fontsize=20)
ax1.set_ylabel('温度',fontsize=20)
plt.title('2000-2015年海底温度曲线对比',fontproperties='SimHei',fontsize=30)
plt.legend(loc='upper right',ncol=2,fontsize = 'large')
plt.savefig('/content/drive/My Drive/plot.png',dpi=200)
