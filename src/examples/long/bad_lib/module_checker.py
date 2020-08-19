"""
This is a module that checks if a library given to it is loadable
(has no undefined references)
"""

import ctypes

libdl = ctypes.CDLL('libdl.so')
lib = None


def check_lib(name):
    x = ctypes.cdll.LoadLibrary(name)
    # noinspection PyProtectedMember
    libdl.dlclose(x._handle)


def load_lib(name):
    global lib
    lib = ctypes.cdll.LoadLibrary(name)
