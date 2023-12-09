"""
Show the size of a data structure in python

We can see that the size of the first array is about 4Mb
which makes sense if each int is 4 bytes.
"""

from itertools import chain
from collections import deque
import reprlib
import sys
import psutil


def total_size(o, handlers=None, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    if handlers is None:
        handlers = {}

    def dict_handler(d):
        return chain.from_iterable(d.items())

    # def object_handler(o):
    #     return o.__dict__.keys()

    def str_handler(s):
        return s

    all_handlers = {
        tuple: iter,
        list: iter,
        deque: iter,
        str: str_handler,
        dict: dict_handler,
        # object: object_handler,
        set: iter,
        frozenset: iter,
    }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object ids have already been seen
    default_size = sys.getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = sys.getsizeof(o, default_size)

        if verbose:
            print(s, type(o), reprlib.repr(o), file=sys.stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)

# my_list = list(range(1000000))


class Person():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.a = [0] * 100

# p = Person("Linus", "Torvalds", 45)
# print(f"my_list size is [{sys.getsizeof(my_list)}]")
# print(f"p size is [{sys.getsizeof(p)}]")
# print(f"my_list size is [{total_size(my_list)}]")
# print(f"p size is [{total_size(p)}]")
# print(dir(p))


l = [0,1,2,3,4,5,6,7,8,9, list(range(10000))]
print(f"total_size of l is [{total_size(l)}]")

print(psutil.virtual_memory())
