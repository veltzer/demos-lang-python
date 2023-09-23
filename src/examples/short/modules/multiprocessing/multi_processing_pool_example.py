"""
This example shows how to use a multiprocessing pool
"""

import multiprocessing
import time


def sleep_a_little(num):
    print("before", num)
    time.sleep(1)
    print("after", num)


with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    for i in range(10):
        pool.apply_async(sleep_a_little, [i])
    pool.join()
