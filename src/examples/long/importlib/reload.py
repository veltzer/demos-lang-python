"""
This is a demo of how to use importlib.reload to reload
modules in python.
"""

import importlib
import time
import my_module.a

while True:
    importlib.reload(my_module.a)
    time.sleep(1)
