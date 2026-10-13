import numpy as np 

arr = np.array([[10,20],[30,40],[50,60]])


arr1 = arr.flatten()#copy 
arr2 = arr.ravel()#view 

arr1[0] = 100
arr2[1] = 200

print(arr)# 
print(arr1)
print(arr2)


array = np.array([1, 2, 3])
padded_array = np.pad(array, pad_width=2, mode='constant',constant_values=100)

print("Padded Array:", padded_array)


#repeat the first and last elements 
array = np.array([1, 2, 3])
padded_array = np.pad(array, pad_width=2, mode='edge')
print("Padded Array:", padded_array)



#repeat the elements around the edges , without repeating the edge itself
array = np.array([1, 2, 3])
padded_array = np.pad(array, pad_width=2, mode='reflect')
print("Padded Array:", padded_array)


#repeat the elements around the edges , without repeating the edge itself
array = np.array([1, 2, 3])
padded_array = np.pad(array, pad_width=2, mode='wrap')
print("Padded Array:", padded_array)



arr= np.array([[1,2],[3,4]])
padded_array = np.pad(arr,2,mode="constant")
print(padded_array)


arr= np.array([[1,2],[3,4]])
padded_array = np.pad(arr,(1,2),mode="constant")
print(padded_array)



#vectorized -- addition 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

ans = arr1 + arr2

print(ans)