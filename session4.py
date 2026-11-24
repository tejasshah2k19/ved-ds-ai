#how to sort in pandas 
#sort_values() vs sort_index()
#Asc - DSC 
#sort using multiple columns 
#ranking rank()
#handeling duplicate values in ranking 


import pandas as pd 

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Rahul", "Priya", "Amit", "Neha",
    "Raj", "Kiran", "Meena", "Jay"
],
"Course": [
    "Python", "Java", "Python", "Java",
    "PHP", "Python", "PHP", "Java"
],
"Age": [21, 22, 20, 23, 21, 24, 22, 20],
"Marks": [88, 90, 65, 95, 72, 55, 88, 40],
"City": [
"Ahmedabad", "Surat", "Rajkot", "Ahmedabad",
"Surat", "Rajkot", "Ahmedabad", "Vadodara"
]
}


df = pd.DataFrame(data)



 
sort_marks = df.sort_values(by="Marks") #return new sorted dataframe 


print(df)
print(sort_marks)

#if you want to modify in original dataframe? 
#inplace=True 
df.sort_values(by="Marks",inplace=True)


#how to sort in descending order ?
#ascending=True => ascending=False 


df = pd.DataFrame(data)
df.sort_values(by="Marks",ascending=False,inplace=True) 
print(df)

df.sort_values(by="Name",ascending=False,inplace=True) #sort by name

#multiple column - with same type of sort 
#sort by name , by marks 
#sort by marks, by name 

df.sort_values(by=["Name","Marks"],ascending=False,inplace=True) #sort by name - marks
 
df.sort_values(by=["Marks","Name"],ascending=False,inplace=True) #sort by name - marks


df.sort_values(by=["Age","Name"],ascending=False,inplace=True) #sort by name - marks
print("----------------------------------")
print(df)
 
#multiple column - with multiple sort 

df.sort_values(by=["Age","Name"],ascending=[False,True],inplace=True)
print("******************************")
print(df)



#sort_index 
#this will sort on index --- index sort 

df = pd.DataFrame(data,index=[1,2,6,7,8,4,5,3])
print("-----------------------\n",df)

df.sort_index(inplace=True)
print("-----------------------\n",df)


#index in desc
df.sort_index(inplace=True,ascending=False)
print("-----------------------\n",df)


df.sort_index(axis=1,inplace=True) #sort column name 
print("-----------------------\n",df)


#sort_values vs sort_index 

#sort on data                          sort on index
#we can have column as param           we have axis 
#can sort by 1 or more column          can sort index/row lable / column lable 
#e.g sort by marks                      sort by index 



#what if we have missing values in data and we want sort ?
#sort with missing values ?
#na_position 

data1 = {
    "Name":["Rock","Jack","Sam","Sakira","Arin"],
    "Marks":[50,None,30,None,85]
} 

df = pd.DataFrame(data1)

df.sort_values(by="Marks",inplace=True,ascending=False)
print(df)

#or 
df.sort_values(by="Marks",inplace=True,ascending=False,na_position="last")
print(df)




df.sort_values(by="Marks",inplace=True,ascending=False,na_position="first")
print(df)


#######################################################
#top 3 students 
#nlargest()

df = pd.DataFrame(data)
result  = df.nlargest(3,"Marks")
print("=======================\n",result)


#nsmallest 
result  = df.nsmallest(3,"Marks")
print("=======================\n",result)


df = pd.DataFrame(data)
result  = df.nlargest(5,"Marks")
print("=======================\n",result)


df = pd.DataFrame(data)
result  = df.nlargest(5,["Marks","Age"])
print("=======================\n",result)



#rank -> rank 1 to n By ASC ORDER 
marks = pd.Series([85,98,80,100])
print(marks.rank())# 

#0  2
#1  3
#2  1
#3  4 

print(marks.rank(ascending=False))# 

#what if we have duplicate values 
marks = pd.Series([85,98,80,98,100])
print(marks.rank())# 

marks = pd.Series([85,98,80,98,98,100])
print(marks.rank())# 

#default ranking on duplicate is average 
marks = pd.Series([85,98,80,98,98,100])
print(marks.rank(method="average"))# 


marks = pd.Series([85,98,80,98,98,100])
print(marks.rank(method="min"))# 


marks = pd.Series([85,98,80,98,98,100])
print(marks.rank(method="max"))# 


marks = pd.Series([85,98,80,98,98,100])
print(marks.rank(method="dense"))# no gap 



############
marks = pd.Series([85,98,80,100])
print("-----------------------------------")
print(marks.rank(ascending=False))#
print(marks.rank(ascending=False,pct=True))#
 
