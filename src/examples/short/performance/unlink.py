"""
this example explores whether it is better to not remove files vs the try/except
paradigm or rather via the os.path.isfile paradigm.

it proves that maintaining a cache in user space is the best approach.
"""

import os.path
import time

count = 1000000
time_before = time.time()
for i in range(count):
    filename = 'unknown' + str(i % 1000) + '.nosuchending'
    try:
        os.unlink(filename)
    except IOError:
        pass
time_after = time.time()
print(f"time taken for {count} os.unlinks+exception handling : {time_after - time_before:.3f} seconds")

time_before = time.time()
for i in range(count):
    filename = f"unknown{i % 1000}.nosuchending"
    if os.path.isfile(filename):
        os.unlink(filename)
time_after = time.time()
print(f"time taken for {count} isfile+unlink : {time_after - time_before:.3f} seconds")

time_before = time.time()
files = {}
for i in range(count):
    filename = f"unknown{i % 1000}.nosuchending"
    if filename not in files:
        if os.path.isfile(filename):
            os.unlink(filename)
            files[filename] = False
        else:
            files[filename] = False
    else:
        if files[filename]:
            os.unlink(filename)
            files[filename] = False
        else:
            pass
time_after = time.time()
print(f"time taken for {count} cached unlink ops : {time_after - time_before:.3f} seconds")
