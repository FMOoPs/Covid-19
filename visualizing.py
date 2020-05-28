from matplotlib import pyplot as plt
import numpy as np
import sqlite3
small = 8
med = 12
plt.rc('axes', titlesize=small)
plt.rc('axes', labelsize=small)
plt.rc('legend', fontsize=small)
plt.rc('xtick', labelsize=small)
plt.rc('ytick', labelsize=small)

#Cases Percentage Pie
conn = sqlite3.connect('WORLD.sqlite')
cur = conn.cursor()
continents = ['Africa', 'Europe', 'NorthAmerica', 'SouthAmerica', 'Asia', 'Australia']
cases = []
for i in range(len(continents)):
    x = cur.execute('SELECT cases FROM continents WHERE continent=?', (str(continents[i]),)).fetchall()
    cases.append(x[0][0])
a = plt.figure(1)
plt.pie(cases,
        labels=continents,
        shadow = True,
        startangle = 90,
        autopct = '%1.1f%%',
        wedgeprops = {'edgecolor': 'white'})
plt.title('Cases percentage each continent')

#Test Chart

tests = []
for i in range(len(continents)):
    x = cur.execute('SELECT tests FROM continents WHERE continent=?', (str(continents[i]),)).fetchall()
    tests.append(x[0][0])
b = plt.figure(2)
plt.pie(tests,
        labels=continents,
        shadow = True,
        startangle = 90,
        autopct = '%1.1f%%',
        wedgeprops = {'edgecolor': 'white'})
plt.title('Cases percentage each continent')


#Recovery Chart
rec = []
per = []
for i in range(len(continents)):
    x = cur.execute('SELECT recovery FROM continents WHERE continent=?', (str(continents[i]),)).fetchall()
    rec.append(x[0][0])
    z = (rec[i]/cases[i])*100
    per.append(z)
c = plt.figure(3)
plt.style.use('fivethirtyeight')
plt.bar(continents, rec)
plt.title('Recovery for each continent')
plt.xlabel('Continents')
plt.ylabel('Recovery')
plt.tight_layout()


#Top 5 (cases, death, Recovery) Chart
country = [] #X-Axis
total = []
death = []
recovery = []
u = cur.execute('SELECT country, total, totdeath, totrecover FROM WORLD ORDER BY total DESC LIMIT 10').fetchall()
for x,y,a,e in u:
    country.append(x)
    total.append(y)
    death.append(a)
    recovery.append(e)
for i in range(len(recovery)):
    if recovery[i] =='N/A': recovery[i] = 0
d = plt.figure(4)
x_indexes = np.arange(len(country))
width = 0.25
plt.bar(x_indexes - width, total, width=width, color='#444444', label='total')
plt.bar(x_indexes , death, width=width, color='#008fd5', label='death')
plt.bar(x_indexes + width, recovery, width=width, color='#e5ae38', label='recovery')
plt.legend()
plt.xticks(ticks=x_indexes, labels=country)
plt.title('Top 5 Countries in Cases')
plt.xlabel('Country')
plt.rcParams.update({'font.size': 4})

plt.show()
