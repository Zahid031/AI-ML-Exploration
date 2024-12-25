#Line Plot
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,-20,30,40,50]
plt.plot(x,y)
# plt.show()
plt.plot([1,2,3,3],[7,8,9,10],label="Trend")
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

#Bar Charts
import matplotlib.pyplot as plt
x=["A","B","C"]
y=[10, 20,5]
plt.bar(x,y,color="green")
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Histogram:show the distribution of a dataset
import matplotlib.pyplot as plt
import numpy as np
data=[1,2,3,3,4,4,4,5,5,5,5,5,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10]
plt.hist(data,bins=5)
plt.title("Histogram")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Scatter Plot
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
