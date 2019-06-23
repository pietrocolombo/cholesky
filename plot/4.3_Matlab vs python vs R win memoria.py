import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math


#________________________________
#matlab memoria

path = '../results/windows/matlab/'
#files = os.listdir(path)
#print(files)
files = ['ex15', 'cfd1', 'shallowwater', 'cfd2', 'parabolicfem', 'apache2', 'G3circuit']#, 'stoc-f']
#files = ['ex15']
result_matlab_win = [0] * files.__len__()
result_matlab_ubuntu = [0] * files.__len__()
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_matlab_win[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

path = '../results/linux/matlab/'
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_matlab_ubuntu[j] = mat

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
result_python_win = [0] * files.__len__()
result_python_ubuntu = [0] * files.__len__()
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_python_win[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

path = '../results/linux/python/'
j = 0
for name in files:
    perc = path + name + '.mat.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_python_ubuntu[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

#________________________________
#R memoria

path = '../results/windows/r/'
#files = os.listdir(path)
#print(files)
files_r_win = ['ex15', 'cfd1', 'shallowwater', 'cfd2', 'parabolicfem']#, 'stoc-f']
#files = ['ex15']
result_r_win = [0] * files_r_win.__len__()

j = 0
for name in files_r_win:
    perc = path + name + '.mtx.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_r_win[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

files_r_ubuntu = ['ex15', 'cfd1', 'shallowwater', 'cfd2', 'parabolicfem', 'apache2']#, 'stoc-f']
result_r_ubuntu = [0] * files_r_ubuntu.__len__()
path = '../results/linux/r/'
j = 0
for name in files_r_ubuntu:
    perc = path + name + '.mtx.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_r_ubuntu[j] = mat

    #print(df['Virtual'].max())
    j = j + 1



# Create bars matlab
barWidth = 0.20
mem_bef_matlab_win = [0] * files.__len__()
mem_after_matlab_win = [0] * files.__len__()
mem_bef_matlab_ubuntu = [0] * files.__len__()
mem_after_matlab_ubuntu = [0] * files.__len__()

for i in range(files.__len__()):
    mem_bef_matlab_win[i] = result_matlab_win[i][2]
    mem_after_matlab_win[i] = result_matlab_win[i][1]

    mem_bef_matlab_ubuntu[i] = result_matlab_ubuntu[i][2]
    mem_after_matlab_ubuntu[i] = result_matlab_ubuntu[i][1]

# Create bars python
barWidth = 0.20
mem_bef_python_win = [0] * files.__len__()
mem_after_python_win = [0] * files.__len__()
mem_bef_python_ubuntu = [0] * files.__len__()
mem_after_python_ubuntu = [0] * files.__len__()

for i in range(files.__len__()):
    mem_bef_python_win[i] = result_python_win[i][2]
    mem_after_python_win[i] = result_python_win[i][1]

    mem_bef_python_ubuntu[i] = result_python_ubuntu[i][2]
    mem_after_python_ubuntu[i] = result_python_ubuntu[i][1]

# Create bars r
barWidth = 0.15
mem_bef_r_win = [0] * files.__len__()
mem_after_r_win = [0] * files.__len__()
mem_bef_r_ubuntu = [0] * files.__len__()
mem_after_r_ubuntu = [0] * files.__len__()

for i in range(files_r_win.__len__()):
    mem_bef_r_win[i] = result_r_win[i][2]
    mem_after_r_win[i] = result_r_win[i][1]

for i in range(files_r_ubuntu.__len__()):
    mem_bef_r_ubuntu[i] = result_r_ubuntu[i][2]
    mem_after_r_ubuntu[i] = result_r_ubuntu[i][1]


# position bars
n = max(len(mem_bef_r_ubuntu),len(mem_after_r_ubuntu),len(mem_bef_r_win),len(mem_after_r_win))
pos = np.arange(n)

bar1 = plt.bar(pos, mem_bef_r_ubuntu, width = barWidth, color = 'r', label='R before Windows')
bar2 = plt.bar(pos+barWidth, mem_after_r_ubuntu, width = barWidth, color = 'b', label='R after Windows')

bar3 = plt.bar(pos+barWidth+barWidth, mem_bef_python_win, width = barWidth, color = 'g', label='Python before Windows')
bar4 = plt.bar(pos+barWidth+barWidth+barWidth, mem_after_python_win, width = barWidth, color = 'y', label='Python after Windows')

bar5 = plt.bar(pos+barWidth * 4, mem_bef_matlab_win, width = barWidth, color = 'g', label='Matlab before Windows')
bar6 = plt.bar(pos+barWidth * 5, mem_after_matlab_win, width = barWidth, color = 'y', label='Matlabafter Windows')

plt.legend(ncol=4,loc='upper left')

plt.xticks([m + barWidth * 2 + barWidth/2 for m in range(len(mem_bef_r_ubuntu))], ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit'])
plt.yscale('log')

for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
'''
for i in range(len(pos)):
    plt.text(x = pos[i] - 0.015, y = mem_bef_matlab_win[i], s = round(mem_bef_matlab_win[i],0), size = 7)
    plt.text(x = pos[i] + barWidth - 0.015, y = mem_after_matlab_win[i], s = round(mem_after_matlab_win[i],0), size = 7)
    plt.text(x = pos[i] + barWidth + barWidth - 0.015, y = mem_bef_matlab_ubuntu[i], s = round(mem_bef_matlab_ubuntu[i],0), size = 7)
    plt.text(x = pos[i] + barWidth + barWidth + barWidth - 0.015, y = mem_after_matlab_ubuntu[i], s = round(mem_after_matlab_ubuntu[i],0), size = 7)
'''
'''
    plt.text(x = pos[i] - 0.015, y = mem_bef_matlab_win[i] + alfa * mem_bef_matlab_win[i], s = round(mem_bef_matlab_win[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth - 0.015, y = mem_after_matlab_win[i] + alfa * mem_after_matlab_win[i], s = round(mem_after_matlab_win[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth + barWidth - 0.015, y = mem_bef_matlab_ubuntu[i] + alfa * mem_bef_matlab_ubuntu[i], s = round(mem_bef_matlab_ubuntu[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth + barWidth + barWidth - 0.015, y = mem_after_matlab_ubuntu[i] + alfa * mem_after_matlab_ubuntu[i], s = round(mem_after_matlab_ubuntu[i],2), size = 7, rotation=90)
'''
#plt.title('Python Ubuntu vs Python Windows with UMF_PACK FALSE')
plt.ylabel('Memory')
plt.xlabel('Matrix Name')

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)

#plt.show()
fig.savefig('../../Grafici/' + os.path.basename(__file__) + '.png', dpi=1000)
