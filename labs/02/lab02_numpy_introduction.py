# numpy - introduction
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.shape)

arr2 = np.array([[1,2, 3], [4, 5, 6]])
print(arr2)
print(arr2.shape) # shape of the matrix
print(arr2.ndim) # dimention of the matrix
print(arr2.size) 

# accessing elments
print(arr2[1,1]) # sec row, sec col
print(arr2[:,0]) # all rows in col 0

m_zeros = np.zeros((2, 3))
m_ones = np.ones(2, 3)

print(np.random.rand(2,2))
print(np.random.randint(-4, 6), size=(3,4))

m_identity = np.identity(3)

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
arr2 = np.repeat(arr, 3)
print(arr2)
