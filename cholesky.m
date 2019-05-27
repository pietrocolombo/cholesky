
x = input('Inserisci nome matrice .mat \n','s');
%f = fullfile('myfolder','mysubfolder','myfile.m');
path = fullfile('../','MatriciCalcoloNumerico',x);
matrix = importdata(path);
A = matrix.A;
size_mat = size(A);
xe = ones(size_mat(1,1),1);
% per misurare il tempo
tic;
b = A * xe;
x = A \ b;
timeElapsed = toc;
error = norm(x - xe)/norm(xe);

% salvataggio infomazioni
fid = fopen( 'matrix.csv', 'a' );

fprintf(fid, '%s', matrix.name, ',');
fprintf(fid, '%s', num2str(size(matrix.A, 1)), ',');
fprintf(fid, '%s', num2str(nnz(matrix.A)), ',');
fprintf(fid, '%s', num2str(error), ',');
fprintf(fid, '%s', num2str(timeElapsed), ',');
fprintf(fid, '1,'); %Positive/Negative
fprintf(fid, 'matlab,');
fprintf(fid, 'windows'); %OS
fprintf(fid, '\n');

fclose(fid);

exit
