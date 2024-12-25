# Panda is a data manipulation python library

import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s)
data={"Name":["Alice","Bob"],"Age":[20,25]}
df=pd.DataFrame(data)
print(df)
print(df.head(1))
print(df.tail(1))
print(df.info)
print(df.describe)
df.to_csv("data.csv")
#df.to_excel("data.xlsx")
#filtering
print(df[df["Age"]>10])

#https://gist.github.com/netj/8836201/#file-iris-csv
#load data from url

import pandas as pd
df=pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
# print(df.head())
# print(df.describe())
# # print(df.tail)
# print("Info\n",df.info())
print(df[["variety","petal.length"]])
filter1=df[(df["variety"]=="Setosa") & (df["petal.length"]>1.5)]
print(filter1)