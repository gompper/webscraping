# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:09:45 2020

@author: urs
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

data = pd.read_csv(url)
data_np = data.to_numpy()

# Accumulate USA 
for i in range(0,len(data_np)):
    if data_np[i][1] == 'US':
        for j in range(4,len(data_np[0])):
            data_np[98][j] = data_np[98][j] + data_np[i][j]


daily = np.empty([len(data),len(data_np[11])-6])
for j in range(0,len(data)):
    for i in range(6,len(data_np[11])):
        daily[j][i-6] = data_np[j][i]
        

        


daily_growth = np.empty([len(data),len(daily[0])-1])    
for j in range(0,len(daily)-1):
    for i in range(0,len(daily[0])-1):
        daily_growth[j][i] = daily[j][i+1] - daily[j][i]    



growth = np.empty([len(daily_growth),len(daily_growth[0])-1])
for j in range(0,len(daily_growth)):
    for i in range(0,len(daily_growth[0])-1):
        if daily_growth[j][i] == 0:
            growth[j][i] = 0
        else:
            growth[j][i] = daily_growth[j][i+1] / daily_growth[j][i]
        
        
plt.figure(1)
plt.subplots_adjust(hspace=0.8)
plt.subplot(311)
plt.axis([0,len(growth[0]),0,5])
plt.plot(growth[120],'o-')
plt.title('Wachstumsfaktor Covid-19 Deutschland')
plt.subplot(312)
plt.axis([0,len(growth[0]),0,5])
plt.plot(growth[28],'o-')
plt.title('Wachstumsfaktor Covid-19 Brasilien')
plt.subplot(313)
plt.axis([0,len(growth[0]),0,5])
plt.plot(growth[98],'o-')
plt.title('Wachstumsfaktor Covid-19 USA')
plt.show()
