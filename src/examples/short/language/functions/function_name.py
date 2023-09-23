"""
This example shows how to find a function name as a string

We show how to find the function name from:
- within the function (sys._getframe().f_code.co_name)
- outside the function (my_func.__name__)
- [function].__qualname__ only works in python3

References:
- http://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
http://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
"""

import inspect
import sys


def my_func():
    print("inside the function")
    print("===================")
    print(f"inspect.stack()[0][0].f_code.co_name is [{inspect.stack()[0][0].f_code.co_name}]")
    print(f"inspect.stack()[0][3] is [{inspect.stack()[0][3]}]")
    print(f"inspect.currentframe().f_code.co_name is [{inspect.currentframe().f_code.co_name}]")
    # noinspection PyProtectedMember
    # pylint: disable=protected-access
    print(f"sys._getframe().f_code.co_name is [{sys._getframe().f_code.co_name}]")


print("outside the function")
print("====================")
print(f"my_func.__name__ is [{my_func.__name__}]")
print(f"my_func.__qualname__ is [{my_func.__name__}]")
print(f"my_func.__module__ is [{my_func.__module__}]")
print(f"my_func is [{my_func}]")
print(f"str(my_func) is [{str(my_func)}]")
my_func()
print("these are the methods that you can call on a function")
print("=====================================================")
print(dir(my_func))
