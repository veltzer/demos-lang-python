""" my_python.py """

import os
from ctypes import CDLL

so_file = os.path.join(os.getcwd(), "my_functions.so")
my_functions = CDLL(so_file)
print(my_functions.square(10))
