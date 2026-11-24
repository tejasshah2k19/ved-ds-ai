#missing data?
#None NaN NaT
#isnull() isna()
#dropna()
#fillna()
#forward fill , backward fill 
#replace()
#interpolation()
#data cleaning 


#None --- python 
#NaN  --- missing value for numerica data  --- not a number 
#NaT  --- missing value for time - date/time value -- not a time
#pd.NA --- pandas missing value marker 

import ui
import pandas as pd 
import numpy as np 

data = {
    "Name":["Sam","Jack",None,pd.NA],
    "Age":[25,np.nan,60,None],
    "Marks":[60,70,pd.NA,90]
} 


df  = pd.DataFrame(data)

print(df)

df["City"]="Ahmedabad"

#how we check we have null value?
#isnull

print(df.isnull())#True -> missing value present 

#count how many -- column wise 
print(df.isnull().sum())

#total -- count total -- scaler 
print(df.isnull().sum().sum())

print("==============================")
print(df.isnull().any())

print("==============================")
print(df.isnull().all())


print("*"*100)

print(df.isna())#True -> missing value present 

#count how many -- column wise 
print(df.isna().sum())

#total -- count total -- scaler 
print(df.isna().sum().sum())

print("==============================")
print(df.isna().any())

print("==============================")
print(df.isna().all())

#isnull() vs isna()
#no functional difference 

#detect not null value
#notnull()

print("==========")
print(df.notnull())

print(df.notnull().sum())
print(df.notnull().sum().sum())
print(df.notnull().any())
print(df.notnull().all())

print("==========")

print(df["Marks"].notnull().sum())

print(df[ df["Marks"].notnull()   ])


print(df[ df["Marks"].notnull() ] )

print(df[ (df["Marks"].notnull())  & (df["Age"].notnull())  ])


#notnull() ---> notna() --> similiar 



######remove missing values 
#dropna()



#default 
result = df.dropna() #axis=0 inPlace=False how="any"


# df.dropna(axis=0,inplace=True,how="any") #row 
#df.dropna(axis=0,inplace=True,how="all") #row 
#print(df)

result = df.dropna(axis=1) #column 
print(result)
print(df)


ui.clear_screen()
#remove row base but condition particular column only 
result = df.dropna(subset=["Marks"])
print(result)

result = df.dropna(subset=["Marks","Age"])
print(result)

#dropna with thresh parameter 
#minimum num of non NAN values required to keep a row or column 

result  = df.dropna(thresh=3)
print(result) 


ui.clear_screen()

#fillna()
#replace missing values (NaN) with another value. 

result = df.fillna(0)
print(result)

result = df.fillna("Not Available")
print(result)


#specific column 
df["Marks"] = df["Marks"].fillna(0)

print(df)

#age 
#mean 
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Age"] = df["Age"].fillna(df["Age"].median())


#fill different values for different columns 
result =df.fillna({
    "Marks":0,
    "Age":18
})

print(result)


#forward fill ----ffill()
#replace missing values with the previous available value 
#backward fill -> bfill()
#replace missing values with the next avaible value 

ui.clear_screen()
stuMarks ={
    "Marks" :[80,90,70,np.nan,60,np.nan,np.nan,80,90,70,np.nan]
    }

df2 = pd.DataFrame(stuMarks)
print(df2)

result = df2.ffill()
print(result)
result= df2.bfill()
print(result)

result = df2.ffill(limit=1) #consecutive missing 
print(result)


#replace()
#replacing specific values -- old value , incorrect value , missing value , NA unknown lable 

ui.clear_screen()
print(df)

# df["Marks"] = df["Marks"].replace(0,80)
# print(df)

# df["Marks"] = df["Marks"].replace({
#     0:70,
#     70:100,
#     60:70
# })

# print(df)

# result =  df.replace("unknown",np.nan)
# print(result)

result =  df.replace(np.nan,"unknown")
print(result)

result =  df.replace(["NA","N/A","n/a","unknown","not available","-"],np.nan)

ui.clear_screen()


data1 = {
    "Days":["Mon","Tue","Wed","Thus","Fri","Sat"],
    "Sales":[1000,1200,np.nan,1600,1500,1700]
}

df3 =  pd.DataFrame(data1)
print(df3)
df3["Sales"]  = df3["Sales"].interpolate()

print(df3)