import numpy as np 


arr = np.eye(4,4,1)
print(arr)



arr = np.eye(4,4,-1)
print(arr)



# diag()

arr = np.diag([10,20,30]) #generate with this values 
print(arr)


arr = np.array([ 
               [10,20,30],
               [40,50,60],
               [70,80,90]
               ])

d = np.diag(arr)
print(d) #extract 

#we can pass k parameter when we generate diag() 


#fromfunction 


#create 1D array with square of index 

#0 1 2 3 4 
#0 1 4 9 16 

arr = np.fromfunction(lambda i: i*i,(5,),dtype=int)
print(arr) 

#2d 
arr = np.fromfunction(lambda i,j: i+j,(3,3),dtype=int)
print(arr)


#multiplication table 

arr = np.fromfunction(lambda i,j: (i+1)*(j+1),(10,10))
print(arr)


def calc(i,j):
    return i*10+j

arr = np.fromfunction(calc,(3,3),dtype=int)
print(arr)


#create array using file data 
#fromfile() -> reads data from an existing file and converts into a numpy array. 
#formats ? text files , binary files

arr = np.fromfile("numbers.txt",sep=" ",dtype=int) 
print(arr)

arr = np.fromfile("numbers.csv",sep=",",dtype=int,count=3) 
print(arr)

 
