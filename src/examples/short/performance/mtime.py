"""
This example explores whether it is efficient or not to cache os.path.getmtime()
data in user space in python.

You can see that os.path.getmtime() in python is *always* a syscall by doing
something like:
    strace ./mtime.py 2>&1 > /dev/null | grep stat64 | grep etc | wc
when running this.

The answer is: YES!!!
"""

import glob
import os.path
import time

count = 1000000
doFirst = True
doSecond = True

# get the list of all files accessible from /etc
files = [f for f in glob.glob('/etc/*') if os.path.isfile(f)]
files.extend([f for f in glob.glob('/etc/*/*') if os.path.isfile(f)])
list_len = len(files)
print(f"file list length is {list_len}...")

# now do lots of os.path.getmtime() ops on them
if doFirst:
    time_before = time.time()
    for i in range(count):
        filename = files[i % list_len]
        os.path.getmtime(filename)
    time_after = time.time()
    print(f"time taken for {count} os.path.getmtime : {time_after - time_before:.3f} seconds")

if doSecond:
    # now do the same with a cache
    times = {}
    time_before = time.time()
    filename = None
    for i in range(count):
        filename = files[i % list_len]
    if filename in times:
        t = times[filename]
    else:
        times[filename] = os.path.getmtime(filename)
    time_after = time.time()
    print(f"time taken for {count} cache getmtime : {time_after - time_before:.3f} seconds")
