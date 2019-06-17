import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math


#f = open("../../Windows Result/Matlab/apache2.txt", "r")

#print(f.readline())
#print(f.readline())


path = '../../Ubuntu Result/Python/UMF_PACK FALSE/'
#files = os.listdir(path)
#print(files)
files = ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit']#, 'stoc-f']
#files = ['ex15']
result_python_ubuntu = [0] * files.__len__()
result_python_win = [0] * files.__len__()
j = 0
for name in files:
    perc = path + name + '_false.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_python_ubuntu[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

path = '../../Windows Result/Python/UMFPACK = false/'
j = 0
for name in files:
    perc = path + name + '_false.txt'
    df = pd.read_table(perc, delim_whitespace=True, skiprows=1, header=None)
    df.columns = ['Elapsed time', 'CPU', 'Real', 'Virtual']
    #print(df)
    mat = [name, df['Virtual'].max(), df['Virtual'][0]]
    result_python_win[j] = mat

    #print(df['Virtual'].max())
    j = j + 1

# print(result_matlab)
# print(result_python)


# Create bars
barWidth = 0.20
mem_bef_python_ubuntu = [0] * files.__len__()
mem_after_python_ubuntu = [0] * files.__len__()
mem_bef_python_win = [0] * files.__len__()
mem_after_python_win = [0] * files.__len__()

for i in range(files.__len__()):
    mem_bef_python_ubuntu[i] = result_python_ubuntu[i][2]
    mem_after_python_ubuntu[i] = result_python_ubuntu[i][1]

    mem_bef_python_win[i] = result_python_win[i][2]
    mem_after_python_win[i] = result_python_win[i][1]
    
# position bars
n = max(len(mem_bef_python_ubuntu),len(mem_after_python_ubuntu),len(mem_bef_python_win),len(mem_after_python_win))
pos = np.arange(n)

plt.bar(pos, mem_bef_python_ubuntu, width = barWidth, color = 'r', label='Python before ubuntu')
plt.bar(pos+barWidth, mem_after_python_ubuntu, width = barWidth, color = 'b', label='Python after ubuntu')

plt.bar(pos+barWidth+barWidth, mem_bef_python_win, width = barWidth, color = 'g', label='Python before win')
plt.bar(pos+barWidth+barWidth+barWidth, mem_after_python_win, width = barWidth, color = 'y', label='Python after win')

plt.legend(ncol=4,loc='upper left')

plt.xticks([m + barWidth + barWidth/2 for m in range(len(mem_bef_python_ubuntu))], ['ex15', 'cfd1', 'shallow_water', 'cfd2', 'parabolic_fem', 'apache2', 'G3_circuit'])

alfa = 0.3
for i in range(len(pos)):
    plt.text(x = pos[i] - 0.015, y = mem_bef_python_ubuntu[i] + alfa * mem_bef_python_ubuntu[i], s = round(mem_bef_python_ubuntu[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth - 0.015, y = mem_after_python_ubuntu[i] + alfa * mem_after_python_ubuntu[i], s = round(mem_after_python_ubuntu[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth + barWidth - 0.015, y = mem_bef_python_win[i] + alfa * mem_bef_python_win[i], s = round(mem_bef_python_win[i],2), size = 7, rotation=90)
    plt.text(x = pos[i] + barWidth + barWidth + barWidth - 0.015, y = mem_after_python_win[i] + alfa * mem_after_python_win[i], s = round(mem_after_python_win[i],2), size = 7, rotation=90)


plt.yscale('log')
plt.title('Python Ubuntu vs Python Windows with UMF_PACK FALSE')
plt.ylabel('Memory')
plt.xlabel('Matrix Name')

plt.show()

