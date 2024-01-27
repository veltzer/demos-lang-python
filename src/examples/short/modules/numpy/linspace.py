import numpy as np

# Create a 2x3 array of all zeros
my_array = np.zeros((2,3))
print(my_array)

# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

# Create an array from a list
my_list = [1, 2, 3]
my_array = np.array(my_list)
print(my_array)

# [1 2 3]

# Generate an array of evenly spaced values
my_linspace = np.linspace(0, 10, 100)
print(my_linspace)
