"""
This example shows what happens when you use multiprocessing
and throw exceptions from the processes.

THIS IS REALLY BAD! NOTHING HAPPENS!
Solution: ALWAYS pass the 'error_callback' parameter with a function
that prints the exceptions.

NOTES:
- in python2 the 'error_callback' feature of the 'apply_async' method
does not exist. Instead use the 'get' method on the value returned
from the import 'apply_async' call.
"""

import multiprocessing
import time


def sleep_a_little(num):
    time.sleep(1)
    raise ValueError('this is bad ' + str(num))


def print_exception(e):
    print('exception happened', e)


with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    for i in range(10):
        pool.apply_async(sleep_a_little, [i], error_callback=print_exception)
    pool.join()
