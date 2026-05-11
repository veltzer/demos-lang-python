"""
This is a module that checks if a library given to it is loadable
(has no undefined references)
"""


import ctypes


def check_lib(name):
    x = ctypes.cdll.LoadLibrary(name)
    # noinspection PyProtectedMember
    # pylint: disable=protected-access
    libdl.dlclose(x._handle)


def load_lib(name):
    return ctypes.cdll.LoadLibrary(name)


lib_name = "libdl.so"
libdl = ctypes.CDLL(lib_name)
lib = load_lib(lib_name)
