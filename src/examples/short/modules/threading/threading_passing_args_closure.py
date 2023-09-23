"""
This is an example of creating a thread and passing it data via its closure
"""

import threading


# this function was written with NO consideratiion of threading...


def func(data):
    print(data)


# this is a wrapper that creates a function with no argument
# that runs any other function with arguments


def create_func(func_to_run, data):
    def wrapper():
        func_to_run(data)

    return wrapper


myfunc = create_func(func, "Hello,World")
t = threading.Thread(target=myfunc)
t.start()
t.join()
