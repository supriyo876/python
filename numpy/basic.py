import numpy as np

"""numbers = np.array([10, 20, 30, 40, 50])

 print(numbers) """

 #  2d arrays 
matrix = np.array([
     [1,2,3],
     [4,5,6]
  ])
print(matrix)

print("shape", matrix.shape)
print("dimention", matrix.ndim)
print("size", matrix.size)
print("data type", matrix.dtype)
print("element 1 is : ", matrix[0,2])


a = ([8,9,6,4,5,4])
print("element 1 is : ", a[0])
print("element 2 is : ", a[1])
print("element 3 is : ", a[2])

#reshaping the array a

print(a.reshape(3, 4))
