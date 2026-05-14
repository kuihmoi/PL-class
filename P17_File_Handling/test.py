import numpy as np

t1 = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
    [[7, 8, 9],
     [6, 5, 4],
     [3, 2, 1]] 
])
print(t1.shape) #output (2, 3, 3) which tells us 2 matrices of 3X3

v1 = np.array([
    [1, 0, -1],
    [-1, 0, 1]
])
print(v1.shape)
try:
    r = np.matvec(t1, v1)
    print(r)
except AttributeError as e:
    print("This np.matvec() is not available in numpy 2.1.0 or earlier.", e)
