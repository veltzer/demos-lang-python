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
    print('inside the function')
    print('===================')
    print('inspect.stack()[0][0].f_code.co_name is [{0}]'.format(inspect.stack()[0][0].f_code.co_name))
    print('inspect.stack()[0][3] is [{0}]'.format(inspect.stack()[0][3]))
    print('inspect.currentframe().f_code.co_name is [{0}]'.format(inspect.currentframe().f_code.co_name))
    # noinspection PyProtectedMember
    print('sys._getframe().f_code.co_name is [{0}]'.format(sys._getframe().f_code.co_name))


print('outside the function')
print('====================')
print('my_func.__name__ is [{0}]'.format(my_func.__name__))
print('my_func.__qualname__ is [{0}]'.format(my_func.__qualname__))
print('my_func.__module__ is [{0}]'.format(my_func.__module__))
print('my_func is [{0}]'.format(my_func))
print('str(my_func) is [{0}]'.format(str(my_func)))
my_func()
print('these are the methods that you can call on a function')
print('=====================================================')
print(dir(my_func))
