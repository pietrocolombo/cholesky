import scipy, scipy.io
import csv
import platform

from datetime import datetime

from scipy.sparse.linalg import norm, spsolve
from scipy.linalg import norm

#name = raw_input("Enter name Matrix") #per python 2.7 raw_input, per 3+ input
name = input("Enter name Matrix")

path = "../MatriciCalcoloNumericoPy/" + name + ".mtx"
print(path)
mat = scipy.io.mmread(path).tocsc()
use_umfpack = True
# type of mat scipy.sparse.csc.csc_matrix
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html

n_rows, n_columns = mat.shape
p_non_zero = mat.nnz / (n_rows * n_columns)
xe = scipy.ones(n_rows)

start_time = datetime.now()
b = mat * xe
if use_umfpack == False:
	print("Evaluating\n...")
	#maybe this is the right format in wich the matrix has to be saved as; https://docs.scipy.org/doc/scipy/reference/sparse.html
	x = spsolve(mat, b, use_umfpack = use_umfpack)
	#x = spsolve(mat, b)
	t = datetime.now() - start_time

	relative_error = norm(x - xe, 2) / norm(xe, 2)
	print("finished!\n")
	with open('matrix_py_false.csv','a') as csvFile:
    	#row = f"{name},{n_rows},{mat.nnz},{relative_error}," + \
    	#        f"{t.seconds}.{t.microseconds},{platform.system()}"
		row = [name, n_rows,n_columns, mat.nnz, relative_error, t.seconds, t.microseconds, platform.system()]
		writer = csv.writer(csvFile)
		writer.writerow(row)
else:
	#maybe this is the right format in wich the matrix has to be saved as; https://docs.scipy.org/doc/scipy/reference/sparse.html
	print("Evaluating\n...")
	x = spsolve(mat, b, use_umfpack = use_umfpack)
	#x = spsolve(mat, b)
	t = datetime.now() - start_time

	relative_error = norm(x - xe, 2) / norm(xe, 2)
	print("finished!")
	with open('matrix_py_true.csv','a') as csvFile:
    	#row = f"{name},{n_rows},{mat.nnz},{relative_error}," + \
    	#        f"{t.seconds}.{t.microseconds},{platform.system()}"
		row = [name, n_rows,n_columns, mat.nnz, relative_error, t.seconds, t.microseconds, platform.system()]
		writer = csv.writer(csvFile)
		writer.writerow(row)


csvFile.close()

print(t)
print(relative_error)

print ("End")