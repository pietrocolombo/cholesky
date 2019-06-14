if(!require(R.matlab)){
   install.packages("R.matlab")
   library("R.matlab")
}
if(!require(rmatio)){
   install.packages("rmatio")
   library("R.matlab")
}

if(!require(optimbase)){
   install.packages("optimbase")
   library("optimbase")
}
 
 if(!require(tictoc)){
    install.packages("tictoc")
    library("tictoc")
}

names <- c('ex15.mtx','cfd1.mtx','shallow_water1.mtx','cfd2.mtx','parabolic_fem.mtx','apache2.mtx','G3_circuit.mtx','Flan_1565.mtx','StocF-1465.mtx')
for (mat in names){
   path <- paste('../../MatriciCalcoloNumericoPy', mat, sep = "/")
   print(path)
   tic()
   matrix <- readMM(path)
   
   size_mat <- dim(matrix)[1]
   xe <- ones(size_mat,1)
   
   tic()
   b <- matrix %*% xe
   
   A.chol <- Cholesky(matrix)
   x <- solve(A.chol, b)
   timeElapsed <- toc()
   
   error <- norm(x - xe)/norm(xe)
   
   csv_write <- data.frame(mat, error, timeElapsed$toc-timeElapsed$tic, .Platform$OS.type)
   if(!file.exists('data.csv')){
      write.table(csv_write,file="data.csv", append=TRUE,sep=",",row.names=FALSE) 
      first_time = FALSE
   }else{
      write.table(csv_write,file="data.csv", append=TRUE,sep=",",col.names=FALSE,row.names=FALSE)
   }
   
}