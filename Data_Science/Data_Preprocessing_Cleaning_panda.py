'''
#drop any missing value rows
df=df.dropna()
#drop column
df=df.dropna(axis=1)
#fill missing value
df.fillna(0)
df["column_name"]=df["column_name"].fillna(0)
df.fillna(method="ffill")#forward fill
df.fillna(method="bfill")#backward fill

#interpolation
df["column_name"]=df["column_name"].interpolate()

#replace
df["column_name"]=df["column_name"].replace(0,5)
df["column_name"]=df["column_name"].replace([0,5],10)

#data transformation

#renaming a column
df=df.rename(columns={"old_name":"new_name"})
#create a new column with specific values
df["new_column"]=df["existing_column"]*2

#concataenation of data frames
concat=pd.concat([df1,df2],axis=0)#row wise
concat=pd.concat([df1,df2,df3],axis=1)#column wisw
#merging data frames
merged=pd.merger(df1,df2,on="column_name")
#joining data frames
joined=df1.join(df2,how="inner")
#grouping data frames
grouped=df.groupby("column_name")
'''

# Creating two simple data sets
import pandas as pd
import numpy as np

data1 = {
    'column_name': [1, 2, 3, 4, 5],
    'value': [10, 20, 30, 40, 50]
}

data2 = {
    'column_name': [1, 2, 3, 6, 7],
    'value': [15, 25, 35, 45, 55]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged=pd.merge(df1,df2,how="outer", on="column_name")
print(merged)