import csv
import platform
import numpy
from datetime import datetime
from scipy import io, linalg
import time

import os, platform
import subprocess

syst = platform.system().lower()
print(syst)

names = ["ex15","cfd1","shallowwater","cfd2","parabolicfem","apache2","G3circuit"]#"Flan_1565","StocF-1465"]
programs = [ "matlab", "python", "r"]
for p in programs:
    for m in names:
        if p == "python":
            m += ".mat"
            cmd = 'python profiler.py --include-children --log results/' + syst + '/python/' + m + '.txt --interval 0.01 '
            cmd += '"python python/cholesky.py ' + m + '"'
            command = subprocess.Popen(cmd, shell = True)
            command.communicate()
        elif p == "matlab":
            print(syst)
            m += ".mat"
            cmd = 'python profiler.py --include-children --log results/' + syst + '/matlab/' + m + '.txt --interval 0.01 '
            if syst == "windows":
                cmd += '"matlab -wait -nodisplay -nosplash -nodesktop -r \\"addpath(genpath(\'matla\'));cd \'matla\';cholesky(\'' + m + '\');exit;\\""'
            elif syst == "linux":
                cmd += '"matlab -wait -nodisplay -nosplash -nodesktop -r \\"addpath(genpath(\'matla\'));cd \'matla\';cholesky(\'' + m + '\');exit;\\""'
            command = subprocess.Popen(cmd, shell = True)
            command.communicate()
            #/usr/local/MATLAB/R2019a/bin/ (matlab alias)
        else:
            print("r")
            m += ".mtx"
            cmd = 'python profiler.py --include-children --log results/' + syst + '/r/' + m + '.txt --interval 0.01 '
            cmd += '"Rscript r/chol.r ' + m + '"'
            command = subprocess.Popen(cmd, shell = True)
            command.communicate()

