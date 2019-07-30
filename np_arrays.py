import numpy as np


#### Creating arrays


### Create your array by directly loading in the data. You can use a list or a tuple. 
### If you want to be super thorough, specify the array type
np_array = np.array([[ 0,  1,  2,  3,  4],
                     [ 5,  6,  7,  8,  9],
                     [10, 11, 12, 13, 14]])
np_array = np.array([(1.5,2,3), (4,5,6)], dtype=float)

### Sometimes, the contents of the initial array may not be known, but we would like 
### to initialise one anyways to use it later. We have a number of functions at out 
### disposal here.

# Creates a 3x4 array of 0's
np.zeros((3,4))

# Creates a 2x3x4 array of int 1's
np.ones((2,3,4), dtype=np.int16) 

# Creates an empty 2x3 array
np.empty((2,3))

### You can also create arrays with certain patterns like so

# Creating a 1D array of numbers from 10 to 30 in increments of 5
np.arange( 10, 30, 5 )

# Creating a 1D array of numbers from 0 to 2 in increments of 0.3
np.arange( 0, 2, 0.3 ) 

# Creating a 1D array of 9 numbers equally spaced from 0 to 2 
np.linspace( 0, 2, 9 ) 


#### Getting array information

# Gets the number of axes (dimensions)
np_array.ndim

# Gets the dimensions of the array
np_array.shape

# The total number of elements of the array 
# (product of all elements # in np_array.shape)
np_array.size

# Describe the type of the elements in the array
np_array.dtype



#### Basic Arithmetic

# In Numpy, arithmetic operators on arrays are always applied elementwise. 
# A new array is filled and returned with the result.

# For example, if we create 2 arrays a and b, and subtract b 
# from a, we will get something like this. Remember that you 
# can NOT do such an operation with arrays of differnt sizes, 
# you'll get an error
a = np.array( [20,30,40,50] )
b = np.array( [0, 1, 2, 3] )
c = a - b
c = [20, 29, 38, 47]

# You can also perform scalar operations elementwise on the entire array
b**2
b = [0, 1, 4, 9]

# Or even apply functions
10*np.sin(a)
a = [ 9.12945251, -9.88031624,  7.4511316 , -2.62374854]

# Remember that operation between arrays are always applied elementwise
a = np.array( [20,30,40,50] )
b = np.array( [0, 1, 2, 3] )
c = a * b
c = [0, 30, 80, 150]

# There are many quick and useful functions in numpy that you will 
# use frequently like these
a = np.array( [20,30,40,50] )
a.max() # 50
a.min() # 20
a.sum() # 140

# If you have a multi-dimensional array, use the "axis" parameter
b = np.arange(12).reshape(3,4)
b = [[ 0,  1,  2,  3],
     [ 4,  5,  6,  7],
     [ 8,  9, 10, 11]]

b.sum(axis=0) # [12, 15, 18, 21]
b.min(axis=1) # [0, 4, 8]
b.cumsum(axis=1) # [[ 0,  1,  3,  6], [ 4,  9, 15, 22], [ 8, 17, 27, 38]]

# And if you need one, here are some more common ones that are a bit "mathy-er"
b = np.arange(3)
b = [0, 1, 2]

np.exp(b) # [ 1.0, 2.71828183, 7.3890561 ]
np.sqrt(b) # [ 0.0 ,  1.0, 1.41421356]
np.floor(np.exp(b)) # [ 1.0, 2.0, 7.0 ]
np.round(np.exp(b)) # [ 1.0, 3.0, 7.0 ]




#### Array Slicing and Shaping

# Numpy arrays can be indexed, sliced and iterated over just like Python lists
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[2] # 2
a[2:5] # [2, 3, 4]
a[-1] # 10
a[:8] # [0, 1, 2, 3, 4, 5, 6, 7]
a[2:] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# We can do the same things with multi-dimensional arrays! Just use commas to separate
b = [[ 0,  1,  2,  3],
     [10, 11, 12, 13],
     [20, 21, 22, 23],
     [30, 31, 32, 33],
     [40, 41, 42, 43]]

b[2,3] # 23
b[0:5, 1] # each row in the second column of b --> [ 1, 11, 21, 31, 41]
b[ : ,1] # same thing as above --> [ 1, 11, 21, 31, 41]
b[1:3, : ] # each column in the second and third row 
           # of b --> [[10, 11, 12, 13], [20, 21, 22, 23]]

# Iterating over multidimensional arrays is done with respect to the first axis
for row in b:
  print(row)
# [0 1 2 3]
# [10 11 12 13]
# [20 21 22 23]
# [30 31 32 33]
# [40 41 42 43]



#### Extra!

### These are all the Numpy data types at your disposal

np.int64 # Signed 64-bit integer types
np.float32 # Standard double-precision floating point
np.complex # Complex numbers represented by 128 floats
np.bool # Boolean type storing TRUE and FALSE values
np.object # Python object type
np.string # Fixed-length string type
np.unicode # Fixed-length unicode type

### Numpy arrays can actually be compared directly just like the arithmetic

a = np.array([1, 2, 3])
b = np.array([5, 4, 3])

# If we compare directly we get a boolean value for each element
a == b # array([False, False, True])
a <= 2 # array([False, True, True])

# If we want to compare the entire arrays, we can use Numpy's built in function
np.array_equal(a, b) # False

# We can sort by axis
c = np.array([[2, 4, 8], [1, 13, 7]])
c.sort(axis=0) # array([[1, 4, 7], [2, 13, 8]])
c.sort(axis=1) # array([[2, 4, 8], [1, 7, 13]])

### Array manipulation is also easy with Numpy built in functions

# Transposing array
d = np.transpose(c)

# Changing array shape
c.ravel() # This flattens the array
c.reshape((3, 2)) # Reshape the array from (2, 3) to (3, 2)

# Adding and removing elements 
np.append(c, d) # Append items in array c to array d
np.insert(a, 1, 5, axis=0) # Insert the number '5' at index 1 on axis 0
np.delete(a,[1], axis=1) # Delete item at index 1, axis 1

# Combining arrays
np.concatenate((c,d),axis=0)  # Concatenate arrays c and d on axis 0
np.vstack((c,d),axis=0)  # Concatenate arrays c and d vertically (row-wise)
np.hstack((c,d),axis=0)  # Concatenate arrays c and d horizontally (column-wise)

