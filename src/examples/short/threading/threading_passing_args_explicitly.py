"""
This is a classic thread creation example.
"""

import threading


# this function was written with NO consideratiion of threading...


def func(data):
    print(data)


t = threading.Thread(target=func, args=('Hello',))
t.start()
t.join()
