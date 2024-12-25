'''
grouped=df.groupby("column_name")
for name,group in grouped:
    print(name)
    print(group)

print(grouped.mean())
print(grouped.sum())
print(grouped.size())
print(grouped.count())
print(grouped.describe())
df.groupby("category_column").agg({"value_column":["mean","max","min"]})

'''

import pandas as pd
data = {
    'Class': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Score': [85, 90, 78, 92, 88, 76],
    'Age': [20, 21, 19, 22, 21, 20]
}

df = pd.DataFrame(data)
print("Original Dataset\n",df)
group=df.groupby("Class").mean()
print(group)
group1=df.groupby("Class").agg(
    {
        "Score":["mean","max","min"],
        "Age":["mean","max","min"],
    }
)
print(group1)