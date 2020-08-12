"""
This example is taken from the following talk:
http://pyvideo.org/video/588/mindblowing-python-gil

Results:
$ python3 --version
Python 3.4.3
$ ./gil_python3.py
time taken for single thread: 8.027 seconds
time taken for two threads: 8.030 seconds

Conclusions:
- in python3 the gil implementation got better. Now the gil is efficient, but unfortunately,
still in place. So you get the performance of just one core. Now you can write multi threaded code.
- alternatives are: write multi-processed code (python has great support for that) or write
single threaded multiplexed code.
- in any case the gil got heavily improved from python2 where is has 50% overhead.
- try to run this example in python2 and see the amazing difference.
"""

import threading
import time

limit = 100000000


def count(n):
    while n > 0:
        n -= 1


# first single thread
time_before = time.time()
count(limit)
count(limit)
time_after = time.time()
print('time taken for single thread: {0:.3f} seconds'.format(
    time_after - time_before,
))

# now two threads
time_before = time.time()
t1 = threading.Thread(target=count, args=(limit,))
t2 = threading.Thread(target=count, args=(limit,))
t1.start()
t2.start()
t1.join()
t2.join()
time_after = time.time()
print('time taken for two threads: {0:.3f} seconds'.format(
    time_after - time_before,
))
