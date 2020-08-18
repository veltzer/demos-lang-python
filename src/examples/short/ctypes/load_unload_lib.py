"""
This is a piece of python code that loads a library and
releases it

You can see that this actually works by using pmap(1) on
the python process and seeing that the library libacl
is no longer there...

References:
http://stackoverflow.com/questions/359498/how-can-i-unload-a-dll-using-ctypes-in-python
"""

import ctypes
import signal

libacl = ctypes.cdll.LoadLibrary('libacl.so')
libdl = ctypes.CDLL('libdl.so')
# noinspection PyProtectedMember
libdl.dlclose(libacl._handle)
while True:
    signal.pause()
