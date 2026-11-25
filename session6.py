import pandas as pd

df = pd.DataFrame({
    "RollNo": [101, 102, 103, 101, 104, 102, 105, 106],
    "Name": ["Rahul", "Priya", "Amit", "Rahul", "Neha", "Priya", "Raj", "Kiran"],
    "Course": ["Python", "Java", "Python", "Python", "Java", "Java", "PHP", "Python"],
    "Marks": [85, 90, 78, 85, 95, 90, 72, 88],
    "City": ["Ahmedabad", "Surat", "Rajkot", "Ahmedabad", "Ahmedabad", "Surat", "Vadodara", "Rajkot"]
})
print(df)


print(df.duplicated())

result = df.duplicated()
print(df[result])


print(df.duplicated().sum())

print(df.duplicated(subset=["City"]).sum())

print(df.duplicated(subset=["Course"]).sum())

#[a-z]
#[A-Z]
#[0-9]
#[ABCD]+
#AABC 
