import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import numpy as np

data = requests.get('https://de.wikipedia.org/wiki/COVID-19-F%C3%A4lle_in_Deutschland#Statistik')
soup = BeautifulSoup(data.text, 'html.parser')


data = []
number = []
start = 0
for tr in soup.find_all('tr'):
    for th in tr.find_all('th'):
        if th.text == 'Zunahme pro Tag':
            start = 1
        if start == 1 :
            if th.text.isnumeric():
                number.append(th.text)
            else:
                if th.text[0].isnumeric():
                    tmp = ''
                    for i in range(0,len(th.text)):
                        if th.text[i].isnumeric():
                            tmp = tmp + th.text[i]
                    number.append(tmp)
                    print(tmp)
 
    if start == 1:
        break

numberArr = np.array([float(i) for i in number])        
plt.plot(numberArr.T)     
plt.show()


