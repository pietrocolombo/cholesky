import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math


#f = open("../../Windows Result/Matlab/apache2.txt", "r")

#print(f.readline())
#print(f.readline())


path = '../../Windows Result/Matlab/'
#files = os.listdir(path)
#print(files)
files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']
#files = ['ex15']
result_matlab = [0] * files.__len__()
result_python = [0] * files.__len__()
j = 0
for name in files:
    perc = path + name + '.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_matlab[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

path = '../../Windows Result/Python/'
j = 0
for name in files:
    perc = path + name + '.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_python[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

# print(result_matlab)
# print(result_python)


# Create bars
barWidth = 0.20
mem_bef_matlab = [0] * files.__len__()
mem_after_matlab = [0] * files.__len__()
mem_bef_python = [0] * files.__len__()
mem_after_python = [0] * files.__len__()

for i in range(files.__len__()):
    mem_bef_matlab[i] = result_matlab[i][2]
    mem_after_matlab[i] = result_matlab[i][1]

    mem_bef_python[i] = result_python[i][2]
    mem_after_python[i] = result_python[i][1]
    
# position bars
n = max(len(mem_bef_matlab),len(mem_after_matlab),len(mem_bef_python),len(mem_after_python))
pos = np.arange(n)

plt.bar(pos, mem_bef_matlab, width = barWidth, color = 'r', label='Matlab before')
plt.bar(pos+barWidth, mem_after_matlab, width = barWidth, color = 'b', label='Matlab after')

plt.bar(pos+barWidth+barWidth, mem_bef_python, width = barWidth, color = 'g', label='python before')
plt.bar(pos+barWidth+barWidth+barWidth, mem_after_python, width = barWidth, color = 'y', label='python after')

plt.legend(ncol=4,loc='upper left')

plt.xticks([m + barWidth + barWidth/2 for m in range(len(mem_bef_matlab))], ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit'])

alfa = 0.3
for i in range(len(pos)):
    plt.text(x = pos[i] - 0.015, y = mem_bef_matlab[i] + alfa * mem_bef_matlab[i], s = round(mem_bef_matlab[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth - 0.015, y = mem_after_matlab[i] + alfa * mem_after_matlab[i], s = round(mem_after_matlab[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth + barWidth - 0.015, y = mem_bef_python[i] + alfa * mem_bef_python[i], s = round(mem_bef_python[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth + barWidth + barWidth - 0.015, y = mem_after_python[i] + alfa * mem_after_python[i], s = round(mem_after_python[i],2), size = 7, rotation=90)


plt.yscale('log')
plt.title('Matlab vs Python Windows')
plt.ylabel('Memory')
plt.xlabel('Matrix Name')

plt.show()

