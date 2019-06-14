import csv
import platform
import cvxopt, cvxpy
import numpy
from datetime import datetime
from scipy import io, linalg
from scipy.sparse.linalg import norm, spsolve
from scipy.linalg import norm
from cvxopt import cholmod, matrix, sparse
from cvxpy.interface import matrix_utilities
import os, platform
import subprocess

syst = platform.system().lower()
print(syst)

names = ["ex15"]#,"cfd1","shallow_water1","cfd2","parabolic_fem","apache2","G3_circuit"] #,"Flan_1565","StocF-1465"]
programs = ["python", "matlab", "r"]
for p in programs:
    for m in names:
        """if p == "python":
            m += ".mat"
            cmd = ("python profiler.py --include-children --log " + m + ".txt --interval 0.01 ")
            cmd += '"python python/cholesky.py ' + m + '"'
            command = subprocess.Popen(cmd, shell = True)
            command.communicate()
        el"""
        if p == "matlab":
            m += ".mat"
            cmd = 'python profiler.py --include-children --log results/' + syst + '/matlab/' + m + '.txt --interval 0.01 '
            cmd += '"matlab -wait -nodisplay -nosplash -nodesktop -r \\"addpath(genpath(\'matla\'));cd \'matla\';cholesky(\'' + m + '\');exit;\\""'
            print(cmd)
            command = subprocess.Popen(cmd, shell = True)
            command.communicate()
        else:
            print("r")

