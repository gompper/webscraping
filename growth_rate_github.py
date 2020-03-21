# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:09:45 2020

@author: urs
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'

data = pd.read_csv(url)
data_np = data.to_numpy()

daily = np.empty(len(data_np[11])-6)
for i in range(6,len(data_np[11])):
    daily[i-6] = data_np[11][i]

daily_growth = np.empty(len(daily)-1)    
for i in range(0,len(daily)-1):
    daily_growth[i] = daily[i+1] - daily[i]    



growth = np.empty(len(daily_growth)-1)
for i in range(0,len(daily_growth)-1):
    if daily_growth[i] == 0:
        growth[i] = 0
    else:
        growth[i] = daily_growth[i+1] / daily_growth[i]
        
        
plt.figure(1)
plt.plot(growth,'o-')
plt.show()
