import numpy as np 

arr = np.array([11,2,33,34,244,66])

print(np.sort(arr)) # it does not modify original array 
print(arr)

#arr -> input array 
#axis ->
#kind -> algo 
#order -> 

print(np.sort(arr)[::-1]) 


arr = np.array([[30,100,20],[90,50,70]])

print(arr)
print(np.sort(arr))#default =>axis =>1 
print(np.sort(arr,axis=0))#0 => column 
print(np.sort(arr,axis=1))#1 => row 

#quicksort
#mergesort
#heapsort
#none -> default 
#stable -> numpy version


print(np.sort(arr,kind='heapsort'))#default =>axis =>1 


#argsort() -> index 

#sort() -> returns sorted values 
#argsort()-> returns sorting indices 


arr = np.array([11,2,33,34,244,66])

print(np.argsort(arr))

#argsort() ---> same as sort()


#lexsort()

names = np.array(["ram","shyam","ravan","shyam"])
dept  = np.array(["hr","mgmt","mgmt","sale"])
salary = np.array([12000,13000,12000,14000])

indices = np.lexsort((names,dept)) 

print("indices => ",indices) 

print("names =>",names[indices])
print("dept =>",dept[indices])
print("salary =>",salary[indices])


#argmax() -> max index 

salary = np.array([12000,13000,12000,14000])
print(np.argmax(salary))
 


arr = np.array([[30,100,20],[90,50,70]])

print(np.argmax(arr,axis=0))

print(np.argmax(arr,axis=1))


#nonzero() -> returns array of index 

arr = np.array([10,20,0,30,0,40,50,0])
print(np.nonzero(arr))
print(arr[np.nonzero(arr)])

#where()
#extract()

