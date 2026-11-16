import pandas as pd 

s1 = pd.Series([10,20,30,40,50])

list = [10,20,30,40,50]
s1 = pd.Series(list)

print(s1)

names = pd.Series(["Ram","shyam","sita"])
print(names)


marks = [80,70,90]

s1 = pd.Series(marks,index=["ram","shyam","sita"])
print(s1)



s1 = pd.Series([90,80,70,60],index=["ram","shyam","sita","ram"])
print(s1)


student= {
    "ram":90,
    "shyam":80,
    "sita":70
}


s1 = pd.Series(student) 
print(s1)


s1= pd.Series(100,index=["India","Japan","USA"])
print(s1)


s1 = pd.Series([10,20,30,40,50])

print(s1[0]) #index 0 => 10  
print(s1[1]) #index 1 => 20 

print("*"*60)
s1 = pd.Series([90,80,70,60],index=["ram","shyam","sita","ram"])
print(s1["ram"])
print(s1["sita"])

x = s1["ram"] #Series 
y = s1["sita"] #value - int 

print(type(x))
print(type(y))

s1 = pd.Series([90,80,70,60])
print(s1[0:2]) # 0,1


s1 = pd.Series([90,80,70],index=["ram","shyam","sita"])
print(s1["ram":"sita"]) # ram shyam sita 

