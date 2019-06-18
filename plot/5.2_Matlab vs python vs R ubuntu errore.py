import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math
import csv

#________________________________
#matlab csv
path_matlab = '../matla/matrix.csv'

files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']

data = pd.read_csv(path_matlab, header=None)

#print(data.head())
data.columns = ['name', 'n_righe', 'non zeri', 'relative_error', "time", "pos", "linguaggio", "os"]

new = data["name"].str.split("/", n = 1, expand = True)

#delete name with /
data["name"]= new[1]
#print(data.head())

data.sort_values(by=['n_righe'], inplace=True)

#print(data.head())
data = data.dropna()

matlab_win = data.loc[data['os']=='windows']
matlab_ubuntu = data.loc[data['os']=='ubuntu']
print(matlab_win)
#matlab_win["time"] = pd.to_numeric(matlab_win["time"])

#________________________________
#python
path_python = '../matrix_python.csv'

files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']

data = pd.read_csv(path_python, header=None)

#print(data.head())
data.columns = ['name', 'relative_error', 't.seconds', 't.microseconds', 'os']

data['t.seconds'] = data['t.seconds'].astype(str)
data['t.microseconds'] = data['t.microseconds'].astype(str)

data['time'] = data['t.seconds'] + '.' + data['t.microseconds']
data["time"] = pd.to_numeric(data["time"])
#new = data["name"].str.split("/", n = 1, expand = True)

#delete name with /
#data["name"]= new[1]
#print(data.head())

#data.sort_values(by=['n_righe'], inplace=True)

#print(data.head())
data = data.dropna()

python_win = data.loc[data['os']=='Windows']
python_ubuntu = data.loc[data['os']=='Linux']
print(python_win)
#python_win["time"] = pd.to_numeric(python_win["time"])

#__________________________________
#R
path_r = '../data_r.csv'

files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']

data = pd.read_csv(path_r, header=None)

#print(data.head())
data.columns = ['name', 'relative_error', 'time', 'mem', "os"]

#new = data["name"].str.split("/", n = 1, expand = True)

#delete name with /
#data["name"]= new[1]
#print(data.head())

#data.sort_values(by=['n_righe'], inplace=True)

#print(data.head())
#data = data.dropna()

r_win = data.loc[data['os']=='windows']
r_ubuntu = data.loc[data['os']=='unix']
print(r_win)
#r_win["time"] = pd.to_numeric(r_win["time"])
#for index, row in data.iterrows():
    #print(row['name'], row['time'])

plt.plot( 'name', 'relative_error', data=matlab_ubuntu, marker='o', markerfacecolor='orange', markersize=6, color='orange', linewidth=2, label='relative error Matlab Windows')
plt.plot( 'name', 'relative_error', data=python_ubuntu, marker='o', markerfacecolor='gold', markersize=6, color='gold', linewidth=2, label='relative error Python Windows')
plt.plot( 'name', 'relative_error', data=r_ubuntu, marker='o', markerfacecolor='red', markersize=6, color='red', linewidth=2, label='relative error R Windows')


plt.legend()
plt.legend(ncol=2,loc='upper left')

plt.yscale('log')
#plt.title('Matlab Ubuntu vs Matlab Windows')
plt.ylabel('relative error')
plt.xlabel('Matrix Name')

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
#plt.show()
fig.savefig('../../Grafici/' + os.path.basename(__file__) + '.png', dpi=1000)