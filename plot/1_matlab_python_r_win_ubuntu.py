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
print(python_ubuntu)
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

#________________________________
#matlab memoria

path = '../results/windows/matlab/'
#files = os.listdir(path)
#print(files)
files = ['ex15', 'cfd1', 'shallowwater', 'cfd2', 'parabolicfem', 'apache2', 'G3circuit']#, 'stoc-f']
#files = ['ex15']
#result_matlab_win = [0] * files.__len__()
#result_matlab_ubuntu = [0] * files.__len__()
name_mat = ['ex15', 'cfd1', 'shallow_water1', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = {'name': [name_mat[j]], 'virtual': [df['Virtual'].max()]}
    if j == 0:
        result_matlab_win = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_matlab_win, mat]
        result_matlab_win = pd.concat(frames)

    #print(df['Virtual'].max())
    j = j + 1

path = '../results/linux/matlab/'
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = {'name': [name_mat[j]], 'virtual': [df['Virtual'].max()]}
    if j == 0:
        result_matlab_ubuntu = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_matlab_ubuntu, mat]
        result_matlab_ubuntu = pd.concat(frames)

    #print(df['Virtual'].max())
    j = j + 1

# print(result_matlab)
# print(result_python)

#________________________________
#python memoria

path = '../results/windows/python/'
#files = os.listdir(path)
#print(files)
files = ['ex15', 'cfd1', 'shallowwater', 'cfd2', 'parabolicfem', 'apache2', 'G3circuit']#, 'stoc-f']
#files = ['ex15']
#result_python_win = [0] * files.__len__()
#result_python_ubuntu = [0] * files.__len__()
name_mat = ['ex15', 'cfd1', 'shallow_water1', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = {'name': [name_mat[j]], 'virtual': [df['Virtual'].max()]}
    #result_python_ubuntu[j] = mat
    if j == 0:
        result_python_ubuntu = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_python_ubuntu, mat]
        result_python_ubuntu = pd.concat(frames)
    #print(df['Virtual'].max())
    j = j + 1

path = '../results/linux/python/'
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = {'name': [name_mat[j]], 'virtual': [df['Virtual'].max()]}
    #result_python_win[j] = mat
    if j == 0:
        result_python_win = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_python_win, mat]
        result_python_win = pd.concat(frames)
    #print(df['Virtual'].max())
    j = j + 1

#________________________________
#R memoria

path = '../results/windows/r/'
#files = os.listdir(path)
#print(files)
files_r_win = ['ex15', 'cfd1', 'shallowwater', 'cfd2', 'parabolicfem']#, 'stoc-f']
#files = ['ex15']
#result_r_win = [0] * files_r_win.__len__()
name_mat = ['ex15', 'cfd1', 'shallow_water1', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']

j = 0
for name in files_r_win:
    perc = path + name + '.mtx.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = {'name': [name_mat[j]], 'virtual': [df['Virtual'].max()]}
    #result_python_win[j] = mat
    if j == 0:
        result_r_win = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_r_win, mat]
        result_r_win = pd.concat(frames)
    #print(df['Virtual'].max())
    j = j + 1

files_r_ubuntu = ['ex15', 'cfd1', 'shallowwater', 'cfd2', 'parabolicfem', 'apache2']#, 'stoc-f']
#result_r_ubuntu = [0] * files_r_ubuntu.__len__()
path = '../results/linux/r/'
j = 0
for name in files_r_ubuntu:
    perc = path + name + '.mtx.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    #mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    mat = {'name': [name_mat[j]], 'virtual': [df['Virtual'].max()]}
    #result_r_ubuntu[j] = mat
    if j == 0:
        result_r_ubuntu = pd.DataFrame(mat)
    else:
        mat = pd.DataFrame(mat)
        frames = [result_r_ubuntu, mat]
        result_r_ubuntu = pd.concat(frames)
    #print(df['Virtual'].max())
    j = j + 1


print(result_python_win.head())
print(result_python_ubuntu.head())


#python_ubuntu['time'] = python_ubuntu['time'].astype(str)
#python_ubuntu['microsecondi'] = python_ubuntu['microsecondi'].astype(str)
#python_ubuntu['time'] = python_ubuntu['time'].str.cat(python_ubuntu['microsecondi'],sep=".")
#python_ubuntu['time'] = python_ubuntu['time'].astype(float)
#
#python_win['time'] = python_win['time'].astype(str)
#python_win['microsecondi'] = python_win['microsecondi'].astype(str)
#python_win['time'] = python_win['time'].str.cat(python_win['microsecondi'],sep=".")
#python_win['time'] = python_win['time'].astype(float)

plt.plot( 'name', 'time', data=python_win, marker='o', markerfacecolor='r', markersize=6, color='r', linewidth=2, label='time Python Windows')
plt.plot( 'name', 'time', data=python_ubuntu, marker='o', markerfacecolor='brown', markersize=6, color='brown', linewidth=2, label='time Python Ubuntu', linestyle='--')

plt.plot( 'name', 'relative_error', data=python_win, marker='o', markerfacecolor='blue', markersize=6, color='blue', linewidth=2, label='Relative error Python Windows')
plt.plot( 'name', 'relative_error', data=python_ubuntu, marker='o', markerfacecolor='magenta', markersize=6, color='magenta', linewidth=2, label='Relative error Python Ubuntu', linestyle='--')

plt.plot( 'name', 'virtual', data=result_python_win, marker='o', markerfacecolor='green', markersize=6, color='green', linewidth=2, label='Memoria Python Windows')
plt.plot( 'name', 'virtual', data=result_python_ubuntu, marker='o', markerfacecolor='olive', markersize=6, color='olive', linewidth=2, label='Memoria Python Ubuntu', linestyle='--')

plt.plot( 'name', 'time', data=matlab_win, marker='o', markerfacecolor='orange', markersize=6, color='orange', linewidth=2, label='time Matlab Windows')
plt.plot( 'name', 'time', data=matlab_ubuntu, marker='o', markerfacecolor='gold', markersize=6, color='gold', linewidth=2, label='time Matlab Ubuntu', linestyle='--')

plt.plot( 'name', 'relative_error', data=matlab_win, marker='o', markerfacecolor='pink', markersize=6, color='pink', linewidth=2, label='Relative error Matlab Windows')
plt.plot( 'name', 'relative_error', data=matlab_ubuntu, marker='o', markerfacecolor='purple', markersize=6, color='purple', linewidth=2, label='Relative error Matlab Ubuntu', linestyle='--')

plt.plot( 'name', 'virtual', data=result_matlab_win, marker='o', markerfacecolor='lime', markersize=6, color='lime', linewidth=2, label='Memoria Matlab Windows')
plt.plot( 'name', 'virtual', data=result_matlab_ubuntu, marker='o', markerfacecolor='blueviolet', markersize=6, color='blueviolet', linewidth=2, label='Memoria Matlab Ubuntu', linestyle='--')


plt.plot( 'name', 'time', data=r_win, marker='o', markerfacecolor='crimson', markersize=6, color='crimson', linewidth=2, label='time R Windows')
plt.plot( 'name', 'time', data=r_ubuntu, marker='o', markerfacecolor='chocolate', markersize=6, color='chocolate', linewidth=2, label='time R Ubuntu', linestyle='--')

plt.plot( 'name', 'relative_error', data=r_win, marker='o', markerfacecolor='cyan', markersize=6, color='cyan', linewidth=2, label='Relative error R Windows')
plt.plot( 'name', 'relative_error', data=r_ubuntu, marker='o', markerfacecolor='orchid', markersize=6, color='orchid', linewidth=2, label='Relative error R Ubuntu', linestyle='--')

plt.plot( 'name', 'virtual', data=result_r_win, marker='o', markerfacecolor='sienna', markersize=6, color='sienna', linewidth=2, label='Memoria R Windows')
plt.plot( 'name', 'virtual', data=result_r_ubuntu, marker='o', markerfacecolor='silver', markersize=6, color='silver', linewidth=2, label='Memoria R Ubuntu', linestyle='--')


print(python_ubuntu)
plt.legend()
plt.legend(ncol=4,loc='upper center', frameon=False, bbox_to_anchor=(0.5, 1.0), bbox_transform=plt.gcf().transFigure)
plt.grid(color='grey', linestyle='-', linewidth=0.1, axis='y')
plt.yscale('log')
#plt.title('Matlab Ubuntu vs Matlab Windows')
plt.ylabel('Errore relativo - Memoria - Tempo')
plt.xlabel('Matrix Name')

#plt.show()
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
#plt.show()
fig.savefig('../../Grafici/' + os.path.basename(__file__) + '.png', dpi=1000)
