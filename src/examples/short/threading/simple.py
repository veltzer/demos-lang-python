"""
A very simple example of python threads

References:
http://www.saltycrane.com/blog/2008/09/simplistic-python-thread-example/
"""

import threading
import time


def worker(number):
    print(f"thread {number} is going to sleep...")
    time.sleep(1)
    print(f"thread {number} is waking up...")


threads = []
print("creating the threads")
for i in range(10):
    threads.append(threading.Thread(target=worker, args=(i,)))
print("launching the threads")
for thread in threads:
    thread.start()
print("joining the threads")
for thread in threads:
    thread.join()
print("done")
