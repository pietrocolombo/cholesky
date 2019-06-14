import os
import scipy, scipy.io

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

names = ["ex15.mat","cfd1.mat","shallow_water1.mat","cfd2.mat","parabolic_fem.mat","apache2.mat","G3_circuit.mat","Flan_1565.mat","StocF-1465.mat"]

for i in names:
	print(i)
	path = "../../MatriciCalcoloNumerico/" + i 
	print("starting "+ i +" evaluation\n")
	start_time = datetime.now()
	matr = matrix_utilities.sparse2cvxopt(io.loadmat(path)['Problem']['A'][0][0])
	xe = matrix(numpy.ones([matr.size[0], 1]))
	b = sparse(matr * xe)
	x = cholmod.splinsolve(matr,b)
	t = datetime.now() - start_time
	print("\nended "+ i +" evaluation")
	# calcolo l'errore relativo 
	relative_error = norm(x - xe, 2) / norm(xe, 2)

	print("Writing stats on csv . . !\n")
	with open('matrix_python.csv','a') as csvFile:
		#row = f"{name},{n_rows},{mat.nnz},{relative_error}," + \
   		#        f"{t.seconds}.{t.microseconds},{platform.system()}"
		row = [i, relative_error, t.seconds, t.microseconds, platform.system()]
		writer = csv.writer(csvFile)
		writer.writerow(row)
	csvFile.close()


print ("End")
