import numpy as np 

#stacking -> combining multiple arrays along a new dimensional arrays. 
#stack()
#hstack()
#vstack()
#dstack()
#column_stack()


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])

arr = np.stack((arr1,arr2,arr3),axis=0)
print(arr)

arr = np.stack((arr1,arr2,arr3),axis=1)
print(arr)

#input arrays must have the same shape whe we use stack()
#we will get ValueError 

#vstack => stacks arrays vertically , placing one row group below another. 
#vertical joining 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.vstack((arr1,arr2)) #1array => row1 2array->row2
print(arr3)


arr2d1 = np.array([  [1,2],[3,4] ])
arr2d2 = np.array([  [5,6],[7,8] ])

arr3 = np.vstack((arr2d1,arr2d2)) 
#we will get below stack in single 2D array 
#array1
#array2 
print(arr3)

#when we use vstack on 2D array , column must be same for all array 


arr2d1 = np.array([  [1,2],[3,4],[5,6] ])
arr2d2 = np.array([  [7,8] ])

arr3 = np.vstack((arr2d1,arr2d2)) 
#we will get below stack in single 2D array 
#array1
#array2 
print(arr3)


#hstack() 
#joining arrays hoirizontally , placing columns side by side 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.hstack((arr1,arr2))
print(arr3)


arr2d1 = np.array([  [1,2],[3,4] ])
arr2d2 = np.array([  [5,6],[7,8] ])
arr3 = np.hstack((arr2d1,arr2d2))
print(arr3)

#for 2D arrays when we use hstack , rows must be same for all array.


#dstack()
#depth axis 
#joins arrays along with the thrid axis 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.dstack((arr1,arr2))
print(arr)#1,3,2



arr2d1 = np.array([  [1,2],[3,4] ])
arr2d2 = np.array([  [5,6],[7,8] ])
arr3 = np.dstack((arr2d1,arr2d2))
print(arr3)#2,2,2 


#column_stack()
#side by side 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.column_stack((arr1,arr2))
print(arr) # 3,2 

#hstack() column_stack() when we stacking two 1D array. 
#hstack 1d => 1d 
#column_stack 1d => 2D 
arr2d1 = np.array([  [1,2],[3,4] ])
arr2d2 = np.array([  [5,6],[7,8] ])
arr3 = np.column_stack((arr2d1,arr2d2))
print(arr3)
#for 2D column_stack behaves like hstack()












