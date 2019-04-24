
matrix = importdata('../MatriciCalcoloNumerico/ex15.mat');
A = matrix.A;
size_mat = size(A)
xe = ones(size_mat(1,1),1);
% per misurare il tempo
tic;
b = A * xe;
x = A \ b;
timeElapsed = toc
error = norm(x - xe)/norm(xe)
