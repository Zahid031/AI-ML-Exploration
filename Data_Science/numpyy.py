import numpy as np
arr=np.array([1,2,3,4])
print(arr)
zeroes=np.ones((2,3))
print(zeroes)

ans=np.arange(0,10,2)
print(ans)

ans=np.linspace(0,10,5)
print(ans)
reshape=arr.reshape(2,2)
print(reshape)


import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
sq=np.array([4,16,36])
print(np.sqrt(sq))
print(np.sum(sq))
print(np.max(sq))
print(np.min(sq))
print(np.mean(sq))
print(np.median(sq))
print(np.std(sq))
print(np.sum(sq,axis=0))

even_numbers = np.arange(0, 51, 2)
print(even_numbers)


import numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
transpose=matrix.T
print(transpose)


#broadcasting
import numpy as np
np.random.seed(1)#seed is used to generate same random numbers
ar1=np.array([1,2,3])
print(ar1+5)
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ar1+matrix)

#random array
ar2=np.random.rand(2,2)
print(ar2)
ar3=np.random.randint(2,5,(2,2))
print(ar3)
dataset=np.random.randint(1,51,size=(5,5))
print(dataset)
dataset[dataset>25]=0
print(dataset)