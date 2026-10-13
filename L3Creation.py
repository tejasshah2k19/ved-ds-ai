#1d
#list 
#2d 
#nd 
import numpy as np 


arr = np.array([1,2,3,4,5])
print(arr.dtype)

arr = np.array([1,2,3,4,5],dtype=np.int16)
print(arr.dtype)

arr2 = np.array(arr) 

arr2[0] = 1000 
print(arr)
print(arr2)


arr2 = np.array(arr,copy=False) # ref 

arr2[0] = 1000 
print(arr)
print(arr2)


arr = np.array([[1,2,3],[4,5,6],[7,8,9]],order='F') #memory layout 
print(arr)

arr2  = np.array(arr,order="K") # 'A' 


"""

    'A' => any 
    'C' => c Row 
    'F' => fortan col 
    'K' => keep 

    'A' 
    numpy -> array -> C F 
    'K'
    C F 
    1 2 3   
    4 5 6
    7 8 9 
    

    1 4 7
    2 5 8
    3 6 9 
"""


#array -> default value zero 
arr = np.zeros(5)
print(arr)

#array -> default value one 
arr = np.ones(5)
print(arr)

arr = np.zeros( (3,3) ) 
print(arr)

arr = np.ones( (3,3) ) 
print(arr)

arr = np.arange(1,10)
print(arr)

arr = np.arange(1,10,2)

arr = np.linspace(1,30,10)# 1 to 30 => 10 
print(arr)
#X X X X X X X X X X X X X X X X X X X X X # 

arr,step = np.linspace(1,30,10,retstep=True)# 1 to 30 => 10 
print(arr)
print(step)  #3.22222 -> 30 


arr,step = np.linspace(1,10,10,retstep=True)# 1 to 30 => 10 
print(arr)
print(step)



x = np.random.rand()
print(x)

x = np.random.rand(5)
print(x)

x = np.random.rand(3,4)
print(x)

