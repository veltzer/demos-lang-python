""" linspace.py """

import numpy as np

# Create a 2x3 array of all zeros
my_array1 = np.zeros((2,3))
print(my_array1)

# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

# Create an array from a list
my_list = [1, 2, 3]
my_array2= np.array(my_list)
print(my_array2)

# [1 2 3]

# Generate an array of evenly spaced values
my_linspace = np.linspace(0, 10, 100)
print(my_linspace)
