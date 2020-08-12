"""
This example shows how to handle the exceptions that happen in a multiprocessing
python process in the main process that launched that process.

The idea is that when you call 'apply_async' you get a "future" object.
When you call 'get' on that object you block until you get it's result.

In order to launch multiple concurrent processes you call 'async_apply'
multiple times and store the "future" objects in an array.
After the processing is done you iterate the array and get all the results.
See below.
"""

import multiprocessing
import time


def sleep_a_little(num):
    time.sleep(1)
    if num % 2 == 1:
        raise ValueError('this is bad ' + str(num))
    else:
        return num


pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
results = []
for i in range(10):
    results.append(pool.apply_async(sleep_a_little, [i]))
pool.close()
pool.join()
for i, result in enumerate(results):
    try:
        r = result.get()
        print(i, r)
    except Exception as e:
        print(i, type(e))
