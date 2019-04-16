
matrix = importdata('MatriciCalcoloNumerico/ex15.mat');
A = matrix.A;
size_mat = size(A)
xe = ones(size_mat(1,1),1);
b = A*xe;

x = A\b;

norm(x-xe)/norm(xe)