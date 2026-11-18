# filter data frame based on condition
# comparison operator 
# AND OR NOT 
# isin()
# between()
# query()
# where() and mask()
# real world problem



import pandas as pd

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": [
        "Rahul", "Priya", "Amit", "Neha",
        "Raj", "Kiran", "Meena", "Jay"
    ],
    "Course": [
        "Python", "Java", "Python", "Java",
        "PHP", "Python", "PHP", "Java"
    ],
    "Age": [21, 22, 20, 23, 21, 24, 22, 20],
    "Marks": [85, 90, 65, 95, 72, 55, 88, 40],
    "City": [
        "Ahmedabad", "Surat", "Rajkot", "Ahmedabad",
        "Surat", "Rajkot", "Ahmedabad", "Vadodara"
    ]
}

df = pd.DataFrame(data)

print(df)


#what is dataframe filtering?
#filtering means selecting only those rows that satisfy a particular condition 

#e.g
#find students who scored more than 80 marks 
#


#comparision operators 
# ==  equal to 
# !=  not equal to 
# >
# <
# >= 
# <= 

#marks greater than 80
print("marks > 80")
print(df)

# result = df["Marks"] > 80 
# print(result) #boolean array 

boolean_array = df["Marks"] > 80
result = df[boolean_array] 

result = df[  df["Marks"] > 80  ]
print(result)

#marks < 70
result = df[  df["Marks"] < 70  ]
print(result)

#string 
#students from Ahmedabad 
print("Ahmedabad")
result = df[  df["City"] ==  "Ahmedabad"  ]
print(result)

print("student not enrolled in python")
result = df[  df["Course"] !=  "Python"  ]
print(result)

print("students age greater than or equal to 22 ")
result = df[  df["Age"] >= 22  ]
print(result)

#important point 
#df["Marks"] > 80 => it returns boolean array 
#boolean indexing 


#multiple condition 
#And & 

print("Score 80+ Age 20+")

result = df[  (df["Marks"] >= 80) & (df["Age"] >= 22)  ]
print(result)

#OR | 

print("Marks > 90 OR Age < 22 ")
result = df[  (df["Marks"] > 90) | (df["Age"] < 22)  ]
print(result)

#Not ~ 
#reverse the boolean condition 

print("Students who are not from Ahmedabad")
result = df[  ~(df["City"] ==  "Ahmedabad")  ]
print(result)

#above we can also using != 
result = df[   df["City"] !=  "Ahmedabad"   ]
print(result)

#usage of isin() function 
#isin functions checkes whether values belongs to a give  list of values. 
#sql in 

#find students enrolled in python or java 
print("Students : Python | Java ")
result = df[   (df["Course"] == "Python") |  (df["Course"] == "Java") ]
print(result)


result = df[  df["Course"].isin( ["Python","Java"] ) ]
print(result)



#find students who are not enrolled in python or java 
result = df[  ~df["Course"].isin( ["Python","Java"] ) ]
print(result)

#between() function 
#filters values withing a specified range. 
#left,right,inclusive : arguments 

#students scores between 35 to 65.
result = df[ (df["Marks"] >= 35 )  & (df["Marks"] <= 65) ]
print(result)

result = df[ df["Marks"].between(35,65) ]
print(result)

#exclude end values 
#inclusive left,right,both,neither
result = df[ df["Marks"].between(35,65,inclusive="neither") ]
print(result)


#query()
#we can filter dataframe based on string expression -- your condition is like statement -- string statement . 

#marks greater than 80 
result = df[ df["Marks"] > 80 ]
print(result)

result = df.query("Marks > 80")
print(result)

#Age greater than 20 and marks above 80+
result = df.query("Age > 20 and Marks > 80")
print(result)

#students from surat 
result = df.query("City == 'Surat'")
print(result)


#students from surat or ahmedabad 
result = df.query("City == 'Surat' or City == 'Ahmedabad' ")
print(result)

#variable inside query() 
print("Variable inside query")
marks_condition = 90
result = df.query("Marks > @marks_condition") #must use @ 
print(result)

##where() function
#functions keeps the values where the condition is True , replace the values with NaN(default) where condition is False. 

result = df["Marks"].where(df["Marks"] > 70)
print(result)

#marks 70+ print 
#<70 replace NaN 

#change the default NaN with 0 
result = df["Marks"].where(df["Marks"] > 70,other=0)
print(result)

#mask() ==> opposite of where 
result = df["Marks"].mask(df["Marks"] > 70,other=0)
print(result)


#Selection of particular column after filtering 

#print only names who got 80+ 
result = df.loc[
    df["Marks"] > 80,
    ["Name", "Marks"]
]

print(result)

result = df.loc[
    df["City"] == "Ahmedabad",
    ["Name", "Course"]
]

print(result)



#Combining Multiple Filtering Techniques
# Find students who:
# - Are enrolled in Python or Java.
# - Have marks between 70 and 100.
# - Are older than 20.
# - Display only Name, Course and Marks.

result = df[
    (df["Course"].isin(["Python", "Java"])) &
    (df["Marks"].between(70, 100)) &
    (df["Age"] > 20)
][["Name", "Course", "Marks"]]

print(result)