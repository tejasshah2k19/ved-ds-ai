import pandas as pd 

data = {
    "Name":["Ram","Shyam","Sita"],
    "Age":[25,26,24],
    "Marks":[80,85,96]
}

df = pd.DataFrame(data)
s1 = pd.Series(data) 

 
print(df)
print(s1)


# data = [
#     ["Name","Ram","Shyam","Sita"],
#     ["Age",25,26,24],
#     ["Marks",80,85,96]
# ]


data = [
    ["Ram",25,85],
    ["Shyam",25,95],
    ["Sita",26,90]
]

df = pd.DataFrame(data,columns=["Name","Age","Marks"])

print(df)



data = {
    "Name":["Ram","Shyam","Sita"],
    "Age":[25,26,24],
    "Marks":[80,85,96]
}

df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data,index=["S1","s2","S3"])
print(df)



print("*"*60)

print(df.index) #                returns row index
print(df.columns)#              return columns names 
print(df.values)#             return data as numpy array 
print(df.dtypes)
print(df.shape)
print(df.size)
print(df.ndim)
print(df.empty) 

print(df.T)#                    transpose data frame 



print("__"*60)
print(df.info())


print("__"*60)
print(df.describe())


print("__"*60)
print(df)
print(df.sum(numeric_only=True))
print(df.nunique())

print("*"*60)
print(df["Name"])

print(type(df["Name"]))

print("*"*60)
print(df.Name)

print("*"*60)

print(df[ ["Name","Marks"] ] )
print( type(df[ ["Name","Marks"] ]) )

print(df["Name"]) #Series 
print(df[["Name"]]) #DataFrame 


print("$"*100)
print(df)

print(df.loc['S1'])
print(df.iloc[0])



print("$"*100)
df = pd.DataFrame(data)
print(df)

print(df.loc[0])
print(df.iloc[0])

print(df.loc[0:2])# 0 1 2 
print(df.iloc[0:2])# 0 1 


#
print("*"*60)
print(df.loc[0:2,["Name","Age"]])



print("*"*60)
print(df["Age"])
print(df.Age)

df["Country"] = "India"
print(df)

df["futureAge"] = df["Age"] + 25 

print(df) 

df["Marks"] = df["Marks"] + 2 

df.loc[0,"Marks"] = 99

df.loc[ df["Marks"] > 80 , "Grade2" ] = 'B'

print(df)

df2 = df.drop("Age",axis=1)

print(df)
print(df2)


#df.drop("Age",axis=1,inplace=True)
#print(df)

#deleing multiple columns 
df.drop(["Age","Grade2"],axis=1,inplace=True)

#axis = 0 =>row 
#axis = 1 => column
#inplace=True -> modify original data frame 

#Renaming columns 
df.rename(columns={
    "Name":"StudentName",
    "Marks":"TotalMarks"
},inplace=True)

print(df)

#change index 
df.set_index("StudentName",inplace=True)
print(df)

df.reset_index(inplace=True)
print(df)
