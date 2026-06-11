import numpy as np

# converting python list to numpy array
arr1 = np.array([1, 2, 3])
print(arr1)

# means 1-D array with 3 elements
print(arr1.shape) 

print(arr1.dtype)

arr2 = np.array([[1, 2], [3, 4]])
print(arr2)
print(arr2.shape)
print(arr2.dtype)

# specialized creation eg: create a [2,3] array
zeros = np.zeros((2, 3))
print(zeros)

ones = np.ones((2, 3))
print(ones)

# create an array of values 0 to 9 with a step of 2
range_array = np.arange(0, 10, 2)
print(range_array)
# create an array of values 0 to 9 with a step of 3
range_array1 = np.arange(0, 10, 3)
print(range_array1)
# create an array of values 0 to 99 with a step of 3
range_array2 = np.arange(2, 100, 3)
print(range_array2)

# linspace that we use a lot
# create some evenly spaced values in a range
# from 2 to 100 will generate 10 numbers
linspace_array = np.linspace(2, 100, 10)
print(linspace_array)

linspace_array1 = np.linspace(0, 10, 100)
print(linspace_array1)

# create a 3 by 3 identity matrix
eye_array = np.eye(3)
print(eye_array)
# create a 8 by 3 identity matrix
eye_array = np.eye(8, 3)
print(eye_array)
# create a 8 by 3 identity matrix starting at second elemetn a[1]
eye_array = np.eye(8, 3, k=1)
print(eye_array)

# NEXT TOPIC: array indexing and slicing
# now we have 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr) 

# accesing elements at row 1 column 2 = 7
print(arr[1, 2])

print(arr[0, 0])

print(arr[2, 3])

# printing only the first row
print(arr[0, :])
print(arr[1, :]) #second
print(arr[2, :]) #third

# going for columns
print(arr[:, 0])
print(arr[:, 1])
print(arr[:, 2])
print(arr[:, 3])

 

print(arr[0:2,])

# try getting elements = 6, 7, 10, 11
print(arr[1:3,1:3]) # hint the after ":" count from 1

#Boolean indexing
#create boolean array where true if element is greater than 5
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)

mask = arr > 5
print(mask)

mask = arr >= 5
print(mask)

mask = arr < 5
print(mask)

# try to select elements where mask is true
print(arr[mask]) #only true elements will be printed

# array of indices for row
indices = np.array([0, 2])
print(arr[indices, :])

# row indices
row_indices = np.array([0, 1]) # accesing element at row 0 col 1
col_indices = np.array([1, 2]) # accesing element at row 1 col 2
print(arr[row_indices, col_indices])

# functions like sqrt and etc

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a)
print("Array a:", a)
print("Array b:", b)

# add elementwise addition
print("Element-wise addition:", a + b)
print("Scalar multiplication:", a * 2) # multiply
print("Square root of elements:", np.sqrt(a)) # square root of a
print("Square of elements:", np.square(a)) # printing squares of a
print("Element-wise multiplication:", a * b) # each element of a multiply b
print("Element-wise division:", a / b) # each element of a divide by b
print("Element-wise power:", a ** b) # each element power of 2

# sum of universal functions
print("sum of elements in a:", np.sum(a))
print("mean of elements in a:", np.mean(a))
print("max of elements in a:", np.max(a))
print("min of elements in a:", np.min(a))

# array manipulation = reshaping arrays
# turning 3 by 2 to 2 by 3
# key for preparing data analysis and machine learning
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr)
print(arr.shape)

# we want to reshape this array to 3, 2
reshaped_arr = arr.reshape(3, 2)
print("Reshaped array: \n", reshaped_arr)

flattened = arr.flatten()
print("Flattened array:", flattened)

#transpose swap rows with column
transposed = arr.T
print("Transposed array:\n", transposed)

#concatenation
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
concat_h = np.hstack((arr1, arr2))
print("Horizontal concatenation:\n", concat_h)
#output:
#  [[1 2 5 6] -> first row of arr2 combined with first row of arr1
#  [3 4 7 8]] -> second row of arr2 combined with first row of arr2

# or we can do the same thing for vertical concatenation
concat_v = np.vstack((arr1, arr2))
print("Vertical concatenation:\n", concat_v)
# output:
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]

# numpy is a base for linear algebra: inverse, eigenvalues and more
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1)
print(arr2)

print(np.dot(arr1, arr2)) #matrix multiplication
(1*5 + 2*7, 1*6 + 2*8, 3*5 + 4*7, 3*6 + 4*8)

#finding determinant
print(np.linalg.det(arr1))
(1*4 - 2*3)

#finding inverse
print(np.linalg.inv(arr1))
adj_arr1 = np.array([[4, -2], [-3, 1]])
inver = (1 / (-2)) * adj_arr1
print("Inverse of arr1:\n", inver)

eigenvalues, eigenvectors = np.linalg.eig(arr1)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Ax = b
b_vec = np.array([5, 11])
x = np.linalg.solve(arr1, b_vec)
print("Solution to Ax = b:", x)
# 1x + 2y = 5
# 3x + 4y = 11

#random number generator
# in simulation and data sampling
np.random.seed(42) # -> set seeds for reproductibility
rand_arr = np.random.rand(2, 3) # difference in rand
print("Random array:\n", rand_arr)

# applying normal distribution
rand_arr = np.random.randn(2, 3) # difference in randn
print("Random array with normal distrbution:\n", rand_arr)

rand_arr = np.random.choice([1, 2, 3, 4, 5], size=(2, 3))
print("Random choice array:\n", rand_arr)

# NEXT TOPIC: statistical operation 
# these functions help to summarize data fast 
data = np.array( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean = np.mean(data)

print("Mean:", mean) # 55/10 = 5.5
print("Median:", np.median(data)) # sum of 5 + 6 then divide by 2 = 5.5
print("Variance:", np.var(data)) #each datapoint minus mean squared divided by n-1
print("Standard Deviation:", np.std(data))
print("Quartiles:", np.percentile(data, [25, 50, 75]))

# NEXT TOPIC: broadcasting is numpy's magic
# let's operate on array of different shapes
# keeps our code clean and fast
# but check the shapes to avoid errors

arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2
print("Original array:\n", arr)
print("Scalar:", scalar)

print(arr + scalar) # 1, 2, 3, 4, 5, 6 all of these + 2
# output:
# [[3 4 5]
# [6 7 8]]

vector = np.array([1, 2, 3])
print(arr + vector)
# output:
# [[2 4 6]
# [5 7 9]]

# save data or load our data into .npyfile
arr = np.array([[1, 2, 3], [4, 5, 6]])
np.save("array.npy",arr)

#then we can load it back and print it as it is
# loaded_arr = np.load('array.npy')
# print("Loaded array:\n", loaded_arr)

# np.savetext('array.txt', arr)
# loaded_txt_arr = np.loadtxt('array.txt')
# print("Loaded array from text file:\n", loaded_txt_arr)

# NEXT TOPIC: structured arrays
# structured arrays are like mini databases
dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
structured_arr = np.array([('Alice', 30, 5.5), ('Bob', 25, 6.0)], dtype=dtype)
print("Structured array:\n", structured_arr)
print("Name column:", structured_arr["name"]) #printing name only
print("Age column:", structured_arr["age"]) #age column

# can compute sin, cosine, exponential
# perfect for scientific calcualtion

angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
print("angles:", angles)
#printing sin of angles
print("Sine of angles:", np.sin(angles))
print("Cosine of angles:", np.cos(angles))
print("Exponential of each angles:", np.exp(angles))
print("Logarithm:", np.log(np.array([1, np.e, np.e**2])))

#NEXT TOPIC: masked arrays
# handle missing or invalid data
# useful for cleaning real world datasets with gaps or errors
data = np.array([1, 2, -999, 4, 5])
masked_data = np.ma.masked_values(data, -999)
print("Masked data:", masked_data)
#Output:
# [1 2 -- 4 5] -> negative will be skipped

# i wanna compute mean and ignore masked values
print("Mean of masked data:", np.ma.mean(masked_data)) # 12 / 4 = 3, -999 ignored

# LAST TOPIC: Fourier Transforms
# core functionality in numpy
# converts time domain signals into frequency domain representations

t = np.linspace(0, 1, 100)
print("t:", t)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2* np.pi * 10 * t)
fft_result = np.fft.fft(signal)
freq = np.fft.fftfreq(len(t), t[1] - t[0])
print("FFT result:", fft_result[:5])