#pip install numpy 

import numpy as np 

print(np)
print(np.__version__)

#why numpy?

#list
#5000 6000 7000 8000 9000
#10% bonus 
#num + 10% 

#vectorized operation 

#you dont need to write loop -- interally numpy will iterate on every element

#python loop -> executed through the python interpreter 

#list + 10  
#python code --> loop ---> object ---> addition --> object ---> next 


#numpy arrays ,  store numerical data in more compact , typed memory layout and operation
#are implmeneted in compiled low level code. 


#list + 10  
#python code --> marks + 10  ---> compiled implementation -> process  --->result   

 
#vectorization does not mean that no iteration. 



#how to create numpy array? 
# we have different differnt function to crate array based on requirement 
# major --> array() 
list = [10,20,30,40]
tuple = (10,20,30,40)
mat =  [ [1,2,3],[4,5,6],[7,8,9]]
mat3 = [ [[1,2,3],[4,5,6]],
        [[7,8,9],[10,11,12]]]
        #2,2,3 
  
arr = np.array([10,20,30])
print(arr)
arr = np.array(list)
print(arr)

arr = np.array(tuple)
print(arr)

arr = np.array([10,20.01,30])
print(arr)


arr = np.array([10,'a',20.01,30])
print(arr)

arr = np.array(mat)
print(arr)
arr = np.array(mat3)
print(arr)



#attributes 
#dtype 

arr = np.array([10,20,30])
print(arr.dtype) #int64  

arr = np.array([10,20.1,30])
print(arr.dtype) #float64  


arr = np.array([10,'20',30])
print(arr.dtype) #float64  


arr = np.array([10,20,30])
print(arr.itemsize) # byte => 8


print(type(arr))


#shape 
print("********************")
arr = np.array([10,20,30])
print(arr.shape) # (3,)
print(arr.ndim)
arr = np.array(mat)  
print(arr.shape) # (3,3)
print(arr.ndim)
arr = np.array(mat3)  
print(arr.shape) # (2,3,3)
print(arr.ndim)


print(arr.size) #total elements 
print(arr.size*arr.itemsize) #total memory 
print(arr.nbytes)







#int64 float64
#numpy data type ? 
#int -> int64
#int64 
#int32
#int16
#int8  
#float
#float64
#float32
#float16
#float8
#uint8  

#bool 
#object_ 

#complex64

print("*********************")
arr = np.array([1,2,3,4])
print(arr.dtype)
arr = np.array([1.1,2,3,4])
print(arr.dtype)
arr = np.array([True,False])
print(arr.dtype)
arr = np.array(["royal","ram","jackson"]) #<U7  {< byte order}{U unicode string }{7 max num of unicode } 
#little-endian < 
#big-endian  > 
print(arr.dtype)


"""
    np.int32 
    
    4 bytes 
    
    305419896
    
    Hexa 
    
    0X12345678 
    
    12 34 56 78 
    BigEndian  {most significant byte first }
    1000 12
    1001 34
    1002 56 
    1003 78 
    
    little-endian {least significant byte first }
    1000 78     1003    12
    1001 56     1002    34
    1002 34     1003    56
    1003 12     1004    78 



    0th 2500 ? 
    1st 2504
    
    0th 2500?
    1st 2496
"""

#int64 
#array() #args - parameter 

arr = np.array([1,2,3,4,5],dtype=np.int16)
print(arr.dtype)

#how to access this numpy array? 
#indexing? 
#yes 

print(arr) # whole array 
print(arr[0])#index 
print(arr[0:3]) #slicing 
print(arr[-1]) #negative 
print(arr[::-1])
print(arr[::2])

print(arr+30)
print(arr)
















