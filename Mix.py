import numpy as np 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])


#concate the arr1 and arr2 into arr3 
arr3 = np.concatenate((arr1,arr2))
print(arr3)



arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[4,5],[6,7]])
arr3 = np.concatenate((arr1,arr2))

print(arr3)

arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)


arr3 = np.concatenate((arr1,arr2),axis=0)
print(arr3)


#can we concate more that 2 arrays? 
#yes 

#dimensions do not match then we can ? 
#axis 


arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6,7],[8,9,10]])

arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)