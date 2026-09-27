import pandas as pd

data = {
    "name" : ["akash","batash","pahar","somudro"],
    "age" : [22,None,24,25],
    "salary" :[3000,3500,None,4000]
}

df= pd.DataFrame(data)
print (df)

#finding missing values
print(df.isna())

#count  missing  values
print(df.isna().sum())

# remove missing values
print(df.dropna())

#fill nall values with 0 mean,median etc

print(df.fillna(0))

"""
Important Pandas commands to remember
Purpose	Code
Find missing values	df.isna()
Count missing values	df.isna().sum()
Remove rows	df.dropna()
Fill values	df.fillna(value)
Mean	df["Age"].mean()
Median	df["Age"].median()
Mode	df["Gender"].mode()[0]

"""