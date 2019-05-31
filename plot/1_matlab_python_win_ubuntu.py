import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math
import csv


# csv matlab

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

matlab_win.drop_duplicates(subset ="name", keep = 'last', inplace = True)
matlab_ubuntu.drop_duplicates(subset ="name", keep = 'last', inplace = True)

print(matlab_win)

print(matlab_ubuntu)

#for index, row in data.iterrows():
    #print(row['name'], row['time'])

# csv python

path = '../../cholesky-opensource/matrix_py_false.csv'

files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']

dataubuntu = pd.read_csv(path, header=None)
dataubuntu.columns =  ['name', 'n_righe', 'n_colonne', 'non zeri', 'error', "time", "microsecondi", "os"]

path = '../../cholesky-opensource/csv windows/matrix_py_false.csv'

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

python_win = data.loc[data['os']=='Windows']
python_ubuntu = data.loc[data['os']=='Linux']

python_win.drop_duplicates(subset ="name", keep = 'last', inplace = True)
python_ubuntu.drop_duplicates(subset ="name", keep = 'last', inplace = True)

print(python_win)

print(python_ubuntu)

# memoria python

path = '../../Ubuntu Result/Python/UMF_PACK FALSE/'
#files = os.listdir(path)
#print(files)
files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']
#files = ['ex15']
#result_python_ubuntu = [0] * files.__len__()
#result_python_win = [0] * files.__len__()
j = 0
for name in files:
    perc = path + name + '_false.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    #mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    mat = {'name': [name], 'virtual': [df['Virtual'].max()]}
    #result_python_ubuntu[j] = mat
    if j == 0:
        result_python_ubuntu = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_python_ubuntu, mat]
        result_python_ubuntu = pd.concat(frames)
    #print(df['Virtual'].max())
    j = j + 1

path = '../../Windows Result/Python/UMFPACK = false/'
j = 0
for name in files:
    perc = path + name + '_false.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    #mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    mat = {'name': [name], 'virtual': [df['Virtual'].max()]}
    #result_python_win[j] = mat
    if j == 0:
        result_python_win = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_python_win, mat]
        result_python_win = pd.concat(frames)
    #print(df['Virtual'].max())
    j = j + 1

# print(result_matlab)
# print(result_python)
print(mat)
print(result_python_win.head())
print(result_python_ubuntu.head())

# memoria matlab

path = '../../Windows Result/Matlab/'
#files = os.listdir(path)
#print(files)
files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']
#files = ['ex15']
#result_matlab_win = [0] * files.__len__()
#result_python_ubuntu = [0] * files.__len__()
j = 0
for name in files:
    perc = path + name + '.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    #mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    mat = {'name': [name], 'virtual': [df['Virtual'].max()]}
    if j == 0:
        result_matlab_win = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_matlab_win, mat]
        result_matlab_win = pd.concat(frames)

    #print(df['Virtual'].max())
    j = j + 1

path = '../../Ubuntu Result/Matlab/'
j = 0
for name in files:
    perc = path + name + '.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = {'name': [name], 'virtual': [df['Virtual'].max()]}
    if j == 0:
        result_matlab_ubuntu = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_matlab_ubuntu, mat]
        result_matlab_ubuntu = pd.concat(frames)

    #print(df['Virtual'].max())
    j = j + 1


print(result_python_win.head())
print(result_python_ubuntu.head())


python_ubuntu['time'] = python_ubuntu['time'].astype(str)
python_ubuntu['microsecondi'] = python_ubuntu['microsecondi'].astype(str)
python_ubuntu['time'] = python_ubuntu['time'].str.cat(python_ubuntu['microsecondi'],sep=".")
python_ubuntu['time'] = python_ubuntu['time'].astype(float)

python_win['time'] = python_win['time'].astype(str)
python_win['microsecondi'] = python_win['microsecondi'].astype(str)
python_win['time'] = python_win['time'].str.cat(python_win['microsecondi'],sep=".")
python_win['time'] = python_win['time'].astype(float)

plt.plot( 'name', 'time', data=python_win, marker='o', markerfacecolor='r', markersize=6, color='r', linewidth=2, label='time Python Windows')
plt.plot( 'name', 'time', data=python_ubuntu, marker='o', markerfacecolor='brown', markersize=6, color='brown', linewidth=2, label='time Python Ubuntu', linestyle='--')

plt.plot( 'name', 'error', data=python_win, marker='o', markerfacecolor='blue', markersize=6, color='blue', linewidth=2, label='Relative error Python Windows')
plt.plot( 'name', 'error', data=python_ubuntu, marker='o', markerfacecolor='magenta', markersize=6, color='magenta', linewidth=2, label='Relative error Python Ubuntu', linestyle='--')


plt.plot( 'name', 'time', data=matlab_win, marker='o', markerfacecolor='orange', markersize=6, color='orange', linewidth=2, label='time Matlab Windows')
plt.plot( 'name', 'time', data=matlab_ubuntu, marker='o', markerfacecolor='gold', markersize=6, color='gold', linewidth=2, label='time Matlab Ubuntu')

plt.plot( 'name', 'error', data=matlab_win, marker='o', markerfacecolor='pink', markersize=6, color='pink', linewidth=2, label='Relative error Matlab Windows')
plt.plot( 'name', 'error', data=matlab_ubuntu, marker='o', markerfacecolor='purple', markersize=6, color='purple', linewidth=2, label='Relative error Matlab Ubuntu', linestyle='--')


plt.plot( 'name', 'virtual', data=result_python_win, marker='o', markerfacecolor='green', markersize=6, color='green', linewidth=2, label='Memoria Python Windows')
plt.plot( 'name', 'virtual', data=result_python_ubuntu, marker='o', markerfacecolor='olive', markersize=6, color='olive', linewidth=2, label='Memoria Python Ubuntu')

plt.plot( 'name', 'virtual', data=result_matlab_win, marker='o', markerfacecolor='lime', markersize=6, color='lime', linewidth=2, label='Memoria Matlab Windows')
plt.plot( 'name', 'virtual', data=result_matlab_ubuntu, marker='o', markerfacecolor='blueviolet', markersize=6, color='blueviolet', linewidth=2, label='Memoria Matlab Ubuntu')


print(python_ubuntu)
plt.legend()
plt.legend(ncol=4,loc='upper center', frameon=False, bbox_to_anchor=(0.5, 1.0), bbox_transform=plt.gcf().transFigure)
plt.grid(color='grey', linestyle='-', linewidth=0.1, axis='y')
plt.yscale('log')
#plt.title('Matlab Ubuntu vs Matlab Windows')
plt.ylabel('Errore relativo - Memoria - Tempo')
plt.xlabel('Matrix Name')

plt.show()
