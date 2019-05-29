import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math
import csv


path = '../matrix.csv'

files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']

data = pd.read_csv(path, header=None)

#print(data.head())
data.columns = ['name', 'n_righe', 'non zeri', 'error', "time", "pos", "linguaggio", "os"]

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

print(matlab_ubuntu)

#for index, row in data.iterrows():
    #print(row['name'], row['time'])


plt.plot( 'name', 'time', data=matlab_win, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label='time Matlab Windows')
plt.plot( 'name', 'time', data=matlab_ubuntu, marker='o', markerfacecolor='red', markersize=12, color='orange', linewidth=4, label='time Matlab Ubuntu')

plt.legend(ncol=2,loc='upper left')
plt.legend()
#plt.yscale('log')
plt.title('Matlab Ubuntu vs Matlab Windows')
plt.ylabel('Time')
plt.xlabel('Matrix Name')

plt.show()
