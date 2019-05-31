import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math
import csv


path = '../../cholesky-opensource/matrix_py_true.csv'

files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']

dataubuntu = pd.read_csv(path, header=None)
dataubuntu.columns =  ['name', 'n_righe', 'n_colonne', 'non zeri', 'error', "time", "microsecondi", "os"]

path = '../../cholesky-opensource/csv windows/matrix_py_true.csv'

datawin = pd.read_csv(path, header=None)
datawin.columns =  ['name', 'n_righe', 'n_colonne', 'non zeri', 'error', "time", "microsecondi", "os"]

frames = [dataubuntu, datawin]
data = pd.concat(frames)
#print(data)

#print(data.head())
data.columns =  ['name', 'n_righe', 'n_colonne', 'non zeri', 'error', "time", "microsecondi", "os"]

#new = data["name"].str.split("/", n = 1, expand = True)

#delete name with /
#data["name"]= new[1]
#print(data.head())

data.sort_values(by=['n_righe'], inplace=True)

#print(data.head())
data = data.dropna()

matlab_win = data.loc[data['os']=='Windows']
matlab_ubuntu = data.loc[data['os']=='Linux']
print(matlab_win)

print(matlab_ubuntu) 

#for index, row in data.iterrows():
    #print(row['name'], row['time'])


plt.plot( 'name', 'time', data=matlab_win, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label='time Python Windows')
plt.plot( 'name', 'time', data=matlab_ubuntu, marker='o', markerfacecolor='red', markersize=12, color='orange', linewidth=4, label='time Python Ubuntu', linestyle='--')

plt.legend()
plt.legend(ncol=2,loc='upper right')

plt.yscale('log')
#plt.title('Python Ubuntu vs Python Windows')
plt.ylabel('Time')
plt.xlabel('Matrix Name')

plt.show()
