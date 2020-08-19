"""
A very simple example of python threads

References:
http://www.saltycrane.com/blog/2008/09/simplistic-python-thread-example/
"""

import threading
import time


def worker(number):
    print('thread {0} is going to sleep...'.format(number))
    time.sleep(1)
    print('thread {0} is waking up...'.format(number))


threads = []
print('creating the threads')
for i in range(10):
    threads.append(threading.Thread(target=worker, args=(i,)))
print('launching the threads')
for thread in threads:
    thread.start()
print('joining the threads')
for thread in threads:
    thread.join()
print('done')
