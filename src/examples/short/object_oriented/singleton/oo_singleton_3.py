"""
This is an improvement on the previous singleton example.
This time we protect against concurrent access.
"""

import threading
import typing


class A:
    instance = None  # type: A

    def __init__(self):
        if A.instance is not None:
            raise Exception('you called the constructor twice!!')
        else:
            # constructor code goes here
            print('in A constructor')
            self.my_attribute = 'value'

    lock = threading.Lock()

    def getInstance() -> typing.Union['A', None]:
        A.lock.acquire()
        if A.instance is None:
            A.instance = A()
        ret = A.instance
        A.lock.release()
        return ret

    getInstance = staticmethod(getInstance)


a1 = A.getInstance()
a2 = A.getInstance()
if a1 is a2:
    print('yes,they are the same instance')
print(a1)
print(a2)
print(dir(a1))
print(dir(a2))
