""" my_python.py """

from ctypes import CDLL
import os
so_file = os.path.join(os.getcwd(), "my_functions.so")
my_functions = CDLL(so_file)
print(my_functions.square(10))
