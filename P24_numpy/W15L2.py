# professor is overseas
# a student from his class yang buat kan lecture

import numpy as np

arr = np.array([1, 2, 3, 4])

zeroes = np.zeros((3, 3))
ones = np.ones((2, 5))
seq = np.arange(0, 10, 2)
grid = np.linspace(0, 1, 5)

matrix = np.array ([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix[1, 2])

print(matrix[0:2, 1:])

#shape manipulation
arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)
print(matrix)

auto_matrix = arr.reshape(-1, 2)
print(auto_matrix)

#######################################################################################################

# import numpy as np

# python_list = list(range(10000000))
# %timeit[x*2 for x in python_list]

# python_list = list(range(10000000))
# %timeit numpy_array * 2

# li